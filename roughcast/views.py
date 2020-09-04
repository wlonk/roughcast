from io import BytesIO
from os.path import basename
from zipfile import ZipFile

from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.utils.text import slugify
from django_registration.exceptions import ActivationError
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import (
    AttachedFile,
    Game,
    InAppNotification,
    Team,
    TeamMembership,
    User,
    Version,
)
from .serializers import (
    AttachedFileSerializer,
    GameSerializer,
    InAppNotificationSerializer,
    LoginSerializer,
    LogoutSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    SelfUserSerializer,
    TeamMembershipSerializer,
    TeamSerializer,
    UserProfileSerializer,
    UserSerializer,
    VerifyEmailSerializer,
    VersionSerializer,
)


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request):
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.token = user.get_or_create_token()
        return Response(SelfUserSerializer(user).data, status=status.HTTP_201_CREATED)


class LoginView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            username = (
                User.objects.filter(username__iexact=serializer.data["username"])
                .get()
                .username
            )
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return Response(
                {"non_field_errors": ["Invalid credentials."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "username": username,
            "password": serializer.data["password"],
        }
        user = authenticate(**data)
        if user is None:
            return Response(
                {"non_field_errors": ["Invalid credentials."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.token = user.get_or_create_token()
        return Response(SelfUserSerializer(user).data, status=status.HTTP_200_OK)


class LogoutView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def create(self, request):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    lookup_value_regex = "[^/]+"

    def get_object(self):
        if self.kwargs["username"] == "me":
            self.kwargs["username"] = self.request.user.username
        return super().get_object()
        # TODO: always serialize self with token and SelfUserSerializer

    # The following are detail-false because they only ever apply to the
    # current user; this does mean that they also all create invalid
    # usernames, as a side-effect.
    @action(detail=False, methods=["get", "put"])
    def profile(self, request):
        profile = request.user.profile
        if request.method == "GET":
            return Response(UserProfileSerializer(instance=profile).data)
        serializer = UserProfileSerializer(instance=profile, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(UserProfileSerializer(instance=profile).data)

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def verify_email(self, request):
        serializer = VerifyEmailSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer.save()
        except ActivationError:
            return Response(
                {"non_field_errors": ["Error verifying email."]},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def reset_password(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(use_https=request.is_secure(), request=request)
        return Response(status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def reset_password_confirm(self, request):
        serializer = PasswordResetConfirmSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(request=request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class InAppNotificationViewSet(ModelViewSet):
    serializer_class = InAppNotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return InAppNotification.objects.filter(user=self.request.user)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "slug"
    lookup_value_regex = "[^/]+"


class TeamMembershipViewSet(ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer


class GameViewSet(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = "slug"
    lookup_value_regex = "[^/]+"


class VersionViewSet(ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    filterset_fields = ("slug", "game__slug")

    @action(detail=True, methods=["get"])
    def archive(self, request, pk=None):
        version = self.get_object()
        all_files = [af.attached_file for af in version.attachedfile_set.all()]

        in_memory = BytesIO()
        zip = ZipFile(in_memory, "a")

        for file in all_files:
            name = basename(file.name)
            content = file.read()
            zip.writestr(name, content)

        # fix for Linux zip files read in Windows
        for file in zip.filelist:
            file.create_system = 0
        zip.close()

        filename = f"{version.game.name} {version.name}"

        response = HttpResponse(content_type="application/zip")
        slug_name = slugify(filename)
        response["Content-Disposition"] = f"attachment; filename={slug_name}.zip"
        in_memory.seek(0)
        response.write(in_memory.read())

        return response


class AttachedFileViewSet(ModelViewSet):
    queryset = AttachedFile.objects.all()
    serializer_class = AttachedFileSerializer
