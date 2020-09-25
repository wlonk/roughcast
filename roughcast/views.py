from io import BytesIO
from os.path import basename
from zipfile import ZipFile

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.urls import NoReverseMatch
from django.utils.text import slugify
from django_registration.exceptions import ActivationError
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ViewSet

from . import email_verification
from .models import (
    AttachedFile,
    Game,
    InAppNotification,
    Subscription,
    Team,
    TeamInvite,
    TeamMembership,
    User,
    Version,
)
from .serializers import (
    AttachedFileSerializer,
    GameSerializer,
    InAppNotificationSerializer,
    LoginSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    SelfUserSerializer,
    SubscriptionSerializer,
    TeamInviteSerializer,
    TeamMembershipSerializer,
    TeamSerializer,
    UserProfileSerializer,
    UserSerializer,
    VerifyEmailSerializer,
    VersionSerializer,
)


class AccountsView(ViewSet):
    def list(self, request):
        # Very approximate hacky way to list all routed actions
        mapped_actions = []
        for action_name in dir(self):
            try:
                if hasattr(getattr(self, action_name), "mapping"):
                    mapped_actions.append(action_name)
            except AttributeError:
                pass
        ret = {}
        for url_name in mapped_actions:
            try:
                url_name_lookup = url_name.replace("_", "-")
                ret[url_name] = reverse(
                    f"accounts-{url_name_lookup}",
                    request=request,
                )
            except NoReverseMatch:  # pragma: nocover
                continue

        return Response(ret)

    @action(detail=False, methods=["get", "put"], permission_classes=(IsAuthenticated,))
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

    @action(detail=False, methods=["post"], permission_classes=(IsAuthenticated,))
    def request_verify_email(self, request):
        email_verification.send_activation_email(request.user, request)
        return Response(status=status.HTTP_202_ACCEPTED)

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

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def register(self, request):
        serializer = RegisterSerializer(data=request.data, context={"request": request})
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        user.token = user.get_or_create_token()
        # @@@ Temporary until we build out make-a-team interface:
        team = Team.objects.create(name=f"Team {user.username}")
        TeamMembership.objects.create(user=user, team=team, is_owner=True)
        # @@@
        return Response(SelfUserSerializer(user).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["post"], permission_classes=(AllowAny,))
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
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


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    lookup_value_regex = "[^/]+"

    def get_object(self):
        # TODO: always serialize self with token and SelfUserSerializer
        if self.kwargs["username"] == "me":
            self.kwargs["username"] = self.request.user.username
        user = super().get_object()
        if user == self.request.user:
            user.token = user.get_or_create_token()
        return user

    def get_serializer_class(self):
        try:
            if self.get_object() == self.request.user:
                return SelfUserSerializer
        except KeyError:
            pass
        return self.serializer_class


class InAppNotificationViewSet(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = InAppNotificationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return InAppNotification.objects.filter(
            user=self.request.user, seen_at__isnull=True
        )


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)


class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    lookup_field = "slug"
    lookup_value_regex = "[^/]+"


class TeamMembershipViewSet(ModelViewSet):
    queryset = TeamMembership.objects.all()
    serializer_class = TeamMembershipSerializer


class TeamInviteViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = TeamInviteSerializer

    # @@@ TODO: Permissions:
    #  - Owners of associated team can create, delete
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TeamInvite.objects.for_user(self.request.user)

    @action(detail=True, methods=["post"])
    def accept(self, request, pk=None):
        invite = self.get_object()
        if request.user.email != invite.to_email:
            return Response(status=status.HTTP_403_FORBIDDEN)

        membership = TeamMembership.objects.create(
            user=request.user,
            team=invite.team,
            is_owner=False,
        )
        invite.delete()
        data = TeamMembershipSerializer(instance=membership).data
        return Response(data, status=status.HTTP_201_CREATED)


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
