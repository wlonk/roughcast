from collections import defaultdict
from io import BytesIO
from os.path import basename, splitext
from zipfile import ZipFile

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.utils.text import slugify
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import AttachedFile, Game, Publisher, PublisherMembership, User, Version
from .serializers import (
    AttachedFileSerializer,
    GameSerializer,
    LoginSerializer,
    LogoutSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    PublisherMembershipSerializer,
    PublisherSerializer,
    SelfUserSerializer,
    UserSerializer,
    VersionSerializer,
)


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

    @action(detail=False)
    def me(self, request):
        if request.user.is_authenticated:
            user = request.user
            user.token = user.get_or_create_token()
            serializer = SelfUserSerializer(instance=user)
            return Response(serializer.data)
        return Response(None)

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


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = "slug"
    lookup_value_regex = "[^/]+"


class PublisherMembershipViewSet(ModelViewSet):
    queryset = PublisherMembership.objects.all()
    serializer_class = PublisherMembershipSerializer


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

        file_names = defaultdict(int)
        for file in all_files:
            name = basename(file.name)
            name_count = file_names[name]
            file_names[name] += 1
            content = file.read()
            formatted_name = name
            if name_count > 0:
                name, ext = splitext(name)
                formatted_name = f"{name} ({name_count}){ext}"
            zip.writestr(formatted_name, content)

        # fix for Linux zip files read in Windows
        for file in zip.filelist:
            file.create_system = 0
        zip.close()

        filename = f"{version.game.name} {version.name}.zip"

        response = HttpResponse(content_type="application/zip")
        slug_name = slugify(filename)
        response["Content-Disposition"] = f"attachment; filename={slug_name}_files.zip"
        in_memory.seek(0)
        response.write(in_memory.read())

        return response


class AttachedFileViewSet(ModelViewSet):
    queryset = AttachedFile.objects.all()
    serializer_class = AttachedFileSerializer
