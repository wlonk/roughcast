from os.path import basename

from django.conf import settings
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import serializers

from .models import AttachedFile, Game, Publisher, PublisherMembership, User, Version
from .serializer_fields import SlugStringField, UserStringField, SlugField


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LogoutSerializer(serializers.Serializer):
    pass


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def send_mail(self, context, to_email):
        subject_template_name = "registration/password_reset_subject.txt"
        email_template_name = "registration/password_reset_email.html"
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(
            subject, body, settings.DEFAULT_FROM_EMAIL, [to_email]
        )
        email_message.send()

    def get_users(self, email):
        active_users = User.objects.filter(email__iexact=email, is_active=True)
        return (u for u in active_users if u.has_usable_password())

    def save(self, use_https=False, request=None):
        """
        Generate a one-use only link for resetting password and send it to the
        user.
        """
        email = self.validated_data["email"]
        current_site = get_current_site(request)
        site_name = current_site.name
        domain = current_site.domain
        for user in self.get_users(email):
            context = {
                "email": user.email,
                "domain": domain,
                "site_name": site_name,
                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                "user": user,
                "token": default_token_generator.make_token(user),
                "protocol": "https" if use_https else "http",
            }
            self.send_mail(
                context, user.email,
            )


class PasswordResetConfirmSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def send_mail(self, user, context):
        subject_template_name = "registration/password_change_subject.txt"
        email_template_name = "registration/password_change_email.html"
        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(
            subject, body, settings.DEFAULT_FROM_EMAIL, [user.email]
        )
        email_message.send()

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            User.DoesNotExist,
            DjangoValidationError,
        ):
            user = None
        return user

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        user = self.get_user(data["uid"])
        msg = (
            "Sorry, your password reset token is not valid or has expired. "
            "Please request another."
        )
        if not user:
            raise serializers.ValidationError(msg)
        valid_token = default_token_generator.check_token(user, data["token"])
        if not valid_token:
            raise serializers.ValidationError(msg)
        return data

    def save(self, request=None):
        password = self.validated_data["password1"]
        user = self.get_user(self.validated_data["uid"])
        user.set_password(password)
        user.save()
        current_site = get_current_site(request)
        site_name = current_site.name
        context = {
            "site_name": site_name,
            "support_email": settings.DEFAULT_SUPPORT_EMAIL,
        }
        self.send_mail(user, context)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "get_full_name",
        )


class SelfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "get_full_name",
            "email",
        )


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "url",
            # "members",
            # "members_id",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    # members = serializers.StringRelatedField(many=True, read_only=True)
    # members_id = serializers.PrimaryKeyRelatedField(
    #     many=True, read_only=True, pk_field=serializers.CharField(), source="members"
    # )


class PublisherMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherMembership
        fields = (
            "id",
            "user",
            "user_id",
            "publisher",
            "publisher_id",
            "is_owner",
        )

    id = serializers.CharField(read_only=True)
    user = UserStringField(queryset=User.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="user"
    )
    publisher = SlugStringField(
        model_class=Publisher, queryset=Publisher.objects.all(),
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="publisher"
    )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "publisher",
            "publisher_id",
            "name",
            "slug",
            "banner",
            "description",
            "user_can_add_versions",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    publisher = SlugStringField(
        model_class=Publisher, queryset=Publisher.objects.all(),
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="publisher"
    )
    user_can_add_versions = serializers.SerializerMethodField()

    def get_user_can_add_versions(self, game):
        user = getattr(self.context.get("request", None), "user")
        return user in game.publisher.members.all()


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = (
            "id",
            "created_by",
            "created_by_setter",
            "game",
            "game_id",
            "publisher",
            "name",
            "slug",
            "changelog",
            "is_public",
            "visible_to",
            "archive_link",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    created_by = UserStringField(read_only=True)
    created_by_setter = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="created_by",
    )
    game = SlugStringField(model_class=Game, queryset=Game.objects.all(),)
    game_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="game"
    )
    publisher = SlugStringField(
        model_class=Publisher, read_only=True, source="game.publisher",
    )
    visible_to = UserStringField(queryset=User.objects.all(), many=True,)
    archive_link = serializers.SerializerMethodField()

    def get_archive_link(self, obj):
        return reverse("version-archive", kwargs={"pk": str(obj.pk)})


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = (
            "id",
            "version",
            "version_id",
            "game",
            "publisher",
            "attached_file",
            "name",
        )

    id = serializers.CharField(read_only=True)
    version = SlugStringField(
        model_class=Version,
        read_only=True,
    )
    version_id = serializers.PrimaryKeyRelatedField(
        queryset=Version.objects.all(),
        pk_field=serializers.CharField(),
        source="version"
    )
    game = SlugStringField(model_class=Game, read_only=True, source="version.game",)
    publisher = SlugStringField(
        model_class=Publisher, read_only=True, source="version.game.publisher",
    )
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return basename(obj.attached_file.url)
