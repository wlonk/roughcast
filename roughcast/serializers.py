from os.path import basename

from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError as DjangoValidationError
from django.core.mail import EmailMultiAlternatives
from django.template import loader
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import serializers

from .models import AlphaTestEmail, AttachedFile, Game, Team, TeamMembership, User, Version
from .serializer_fields import SlugField, SlugStringField, UserStringField
from .text import unmark

from . import email_verification


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    tos = serializers.BooleanField()

    def validate_username(self, value):
        if User.objects.filter(username__iexact=value).exists():
            raise serializers.ValidationError("This username is taken.")
        return value

    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("This email is taken.")
        if not AlphaTestEmail.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Sorry, this email is not in the alpha test yet.")
        return value

    def validate_tos(self, value):
        if not value:
            raise serializers.ValidationError("You must accept the terms of service.")
        return value

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Passwords don't match.")
        validate_password(data["password1"])
        return data

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password1"],
        )
        email_verification.send_activation_email(user, self.context["request"])
        return user


class VerifyEmailSerializer(serializers.Serializer):
    key = serializers.CharField()

    def save(self):
        key = self.validated_data["key"]
        email_verification.activate(key)


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
            "token",
        )


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "slug",
            "description",
            "url",
            "permissions",
            "user_is_owner",
            "user_is_member",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, team):
        user = getattr(self.context.get("request", None), "user")
        return {
            "game:add": user in team.members.all(),
            "this:edit": user in team.members.all(),
        }

    user_is_owner = serializers.SerializerMethodField()

    def get_user_is_owner(self, team):
        user = getattr(self.context.get("request", None), "user")
        return (
            user
            and user.is_authenticated
            and TeamMembership.objects.filter(
                user=user, team=team, is_owner=True,
            ).exists()
        )

    user_is_member = serializers.SerializerMethodField()

    def get_user_is_member(self, team):
        user = getattr(self.context.get("request", None), "user")
        return (
            user
            and user.is_authenticated
            and TeamMembership.objects.filter(
                user=user, team=team,
            ).exists()
        )

    def create(self, validated_data):
        team = super().create(validated_data)
        user = getattr(self.context.get("request", None), "user")
        if user and user.is_authenticated:
            TeamMembership.objets.create(
                user=user, team=team, is_owner=True,
            )
        return team


class TeamMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMembership
        fields = (
            "id",
            "user",
            "user_id",
            "team",
            "team_id",
            "is_owner",
        )

    id = serializers.CharField(read_only=True)
    user = UserStringField(queryset=User.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="user"
    )
    team = SlugStringField(
        model_class=Team, queryset=Team.objects.all(),
    )
    team_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="team"
    )


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = (
            "id",
            "team",
            "team_id",
            "name",
            "slug",
            "banner",
            "description",
            "latest_version",
            "permissions",
            "default_visible_to",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    team = SlugStringField(
        model_class=Team, queryset=Team.objects.all(),
    )
    team_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="team"
    )
    default_visible_to = UserStringField(queryset=User.objects.all(), many=True)
    permissions = serializers.SerializerMethodField()

    def get_permissions(self, game):
        user = getattr(self.context.get("request", None), "user")
        return {
            "version:add": user in game.team.members.all(),
            "this:delete": user in game.team.members.all(),
            "this:edit": user in game.team.members.all(),
        }

    latest_version = serializers.SerializerMethodField()

    def get_latest_version(self, game):
        version = game.version_set.first()
        return {
            "name": version.name if version else None,
            "slug": version.slug if version else None,
        }


class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = (
            "id",
            "created_by",
            "created_by_setter",
            "game",
            "game_id",
            "team",
            "name",
            "slug",
            "changelog",
            "changelog_short",
            "is_public",
            "visible_to",
            "archive_link",
            "permissions",
        )

    id = serializers.CharField(read_only=True)
    slug = SlugField()
    created_by = UserStringField(read_only=True)
    created_by_setter = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), source="created_by",
    )
    game = SlugStringField(model_class=Game, queryset=Game.objects.all())
    game_id = serializers.PrimaryKeyRelatedField(
        read_only=True, pk_field=serializers.CharField(), source="game"
    )
    team = SlugStringField(
        model_class=Team, read_only=True, source="game.team",
    )
    visible_to = UserStringField(queryset=User.objects.all(), many=True)
    archive_link = serializers.SerializerMethodField()

    def get_archive_link(self, version):
        return reverse("version-archive", kwargs={"pk": str(version.pk)})

    changelog_short = serializers.SerializerMethodField()

    def get_changelog_short(self, version):
        """Render the changelog, strip it down to its text, and cut it off short.

        We could probably do this on the frontend, but this was easier for me?
        """
        cap = 60
        unmarked = unmark(version.changelog)
        if len(unmarked) > cap:
            unmarked = unmarked[:cap] + "…"
        return unmarked

    permissions = serializers.SerializerMethodField()

    def get_permissions(self, version):
        user = getattr(self.context.get("request", None), "user")
        return {
            "this:delete": user in version.game.team.members.all(),
            "this:edit": user in version.game.team.members.all(),
        }


class AttachedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttachedFile
        fields = (
            "id",
            "version",
            "version_id",
            "game",
            "team",
            "attached_file",
            "name",
        )

    id = serializers.CharField(read_only=True)
    version = SlugStringField(model_class=Version, read_only=True)
    version_id = serializers.PrimaryKeyRelatedField(
        queryset=Version.objects.all(),
        pk_field=serializers.CharField(),
        source="version",
    )
    game = SlugStringField(model_class=Game, read_only=True, source="version.game")
    team = SlugStringField(
        model_class=Team, read_only=True, source="version.game.team",
    )
    name = serializers.SerializerMethodField()

    def get_name(self, attached_file):
        return basename(attached_file.attached_file.url)
