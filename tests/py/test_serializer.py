from unittest.mock import MagicMock, patch

import pytest
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from rest_framework import serializers

from roughcast.serializers import (
    AttachedFileSerializer,
    GameSerializer,
    PasswordResetConfirmSerializer,
    PasswordResetSerializer,
    RegisterSerializer,
    TeamSerializer,
    VerifyEmailSerializer,
    VersionSerializer,
)


@pytest.mark.django_db
class TestRegisterSerializer:
    def test_validate_username(self, user_factory):
        user_factory(username="fantomah")
        with pytest.raises(serializers.ValidationError):
            RegisterSerializer().validate_username("Fantomah")
        assert RegisterSerializer().validate_username("Fantomah2") == "Fantomah2"

    def test_validate_email(self, user_factory, alpha_test_email_factory):
        alpha_test_email_factory(email="stardust@example.com")
        user_factory(email="fantomah@example.com")
        with pytest.raises(serializers.ValidationError):
            RegisterSerializer().validate_email("Fantomah@example.com")
        with pytest.raises(serializers.ValidationError):
            RegisterSerializer().validate_email("spacesmith@example.com")
        assert (
            RegisterSerializer().validate_email("Stardust@example.com")
            == "Stardust@example.com"
        )

    def test_validate_tos(self):
        with pytest.raises(serializers.ValidationError):
            RegisterSerializer().validate_tos(False)
        assert RegisterSerializer().validate_tos(True)

    def test_validate(self):
        with pytest.raises(serializers.ValidationError):
            RegisterSerializer().validate({"password1": "foo", "password2": "bar"})
        data = {
            "password1": "compl3Xpassword",
            "password2": "compl3Xpassword",
        }
        assert RegisterSerializer().validate(data) == data

    def test_create(self, mailoutbox, alpha_test_email_factory):
        data = {
            "username": "bigredmclane",
            "email": "bigredmclane@example.com",
            "password1": "compl3Xpassword",
            "password2": "compl3Xpassword",
            "tos": True,
        }
        alpha_test_email_factory(email="bigredmclane@example.com")
        serializer = RegisterSerializer(data=data, context={"request": MagicMock()})
        assert serializer.is_valid(), serializer.errors
        user = serializer.save()
        assert user is not None
        assert len(mailoutbox) == 1


class TestVerifyEmailSerializer:
    def test_save(self):
        serializer = VerifyEmailSerializer(data={"key": "123abc"})
        assert serializer.is_valid(), serializer.errors
        with patch("roughcast.serializers.email_verification.activate") as activate:
            serializer.save()
            assert activate.called


@pytest.mark.django_db
class TestPasswordResetSerializer:
    def test_send_mail(self, mailoutbox):
        serializer = PasswordResetSerializer()
        context = {
            "uid": "uid",
            "token": "token",
        }
        serializer.send_mail(context, "test@example.com")
        assert len(mailoutbox) == 1

    def test_get_users(self, user_factory):
        user = user_factory(email="test@example.com")
        user.set_password("foobar")
        user_factory()

        serializer = PasswordResetSerializer()
        assert list(serializer.get_users("test@example.com")) == [user]

    def test_save(self, user, mailoutbox):
        data = {"email": user.email}
        serializer = PasswordResetSerializer(data=data)
        assert serializer.is_valid(), serializer.errors
        with patch("roughcast.serializers.get_current_site") as get_current_site:
            get_current_site.return_value = MagicMock(
                name="Roughcast",
                domain="roughcast.app",
            )
            serializer.save()

        assert len(mailoutbox) == 1


@pytest.mark.django_db
class TestPasswordResetConfirmSerializer:
    def test_send_mail(self, mailoutbox, user):
        serializer = PasswordResetConfirmSerializer()
        context = {
            "uid": "uid",
            "token": "token",
        }
        serializer.send_mail(user, context)
        assert len(mailoutbox) == 1

    def test_get_user(self, user):
        serializer = PasswordResetConfirmSerializer()
        uidb64 = urlsafe_base64_encode(str(user.pk).encode("utf-8"))
        assert serializer.get_user(uidb64) == user
        uidb64 = urlsafe_base64_encode("0".encode("utf-8"))
        assert serializer.get_user(uidb64) is None

    def test_validate__bad_passwords(self):
        data = {
            "uid": "uid",
            "token": "token",
            "password1": "foo",
            "password2": "bar",
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        assert not serializer.is_valid()

    def test_validate__bad_uid(self):
        uidb64 = urlsafe_base64_encode("0".encode("utf-8"))
        data = {
            "uid": uidb64,
            "token": "token",
            "password1": "foobar",
            "password2": "foobar",
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        assert not serializer.is_valid()

    def test_validate__bad_token(self, user):
        uidb64 = urlsafe_base64_encode(str(user.pk).encode("utf-8"))
        data = {
            "uid": uidb64,
            "token": "token",
            "password1": "foobar",
            "password2": "foobar",
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        assert not serializer.is_valid()

    def test_validate__good(self, user):
        uidb64 = urlsafe_base64_encode(str(user.pk).encode("utf-8"))
        token = default_token_generator.make_token(user)
        data = {
            "uid": uidb64,
            "token": token,
            "password1": "foobar",
            "password2": "foobar",
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        assert serializer.is_valid()

    def test_save(self, user, mailoutbox):
        uidb64 = urlsafe_base64_encode(str(user.pk).encode("utf-8"))
        token = default_token_generator.make_token(user)
        data = {
            "uid": uidb64,
            "token": token,
            "password1": "foobar",
            "password2": "foobar",
        }
        serializer = PasswordResetConfirmSerializer(data=data)
        assert serializer.is_valid()
        with patch("roughcast.serializers.get_current_site") as get_current_site:
            get_current_site.return_value = MagicMock(
                name="Roughcast",
                domain="roughcast.app",
            )
            serializer.save()

        assert len(mailoutbox) == 1
        user.refresh_from_db()
        assert user.check_password("foobar")


@pytest.mark.django_db
class TestTeamSerializer:
    def test_permissions(self, team):
        serializer = TeamSerializer(instance=team)
        assert serializer.data["permissions"] == {
            "game:add": False,
            "this:edit": False,
        }

    def test_user_is_owner(self, team):
        serializer = TeamSerializer(instance=team)
        assert not serializer.data["user_is_owner"]

    def test_user_is_member(self, team):
        serializer = TeamSerializer(instance=team)
        assert not serializer.data["user_is_member"]

    def test_create(self, user):
        data = {
            "name": "Test Team",
            "slug": "test-team",
            "description": "A test team.",
            "url": "https://example.com/",
        }
        serializer = TeamSerializer(
            data=data, context={"request": MagicMock(user=user)}
        )
        assert serializer.is_valid(), serializer.errors
        team = serializer.save()
        assert team is not None


@pytest.mark.django_db
class TestGameSerializer:
    def test_permissions(self, game):
        serializer = GameSerializer(instance=game)
        assert serializer.data["permissions"] == {
            "version:add": False,
            "this:delete": False,
            "this:edit": False,
        }

    def test_latest_version(self, version):
        serializer = GameSerializer(instance=version.game)
        assert serializer.data["latest_version"] == {
            "name": version.name,
            "slug": version.slug,
        }


@pytest.mark.django_db
class TestVersionSerializer:
    def test_changelog_short(self, version_factory):
        changelog = """\
# This is a heading

This is a paragraph, with a lot of _text_. I think that if
it is long enough, it will get cropped.
        """
        version = version_factory(changelog=changelog)
        serializer = VersionSerializer(instance=version)
        expected = "This is a heading This is a paragraph, with a lot of text. "
        assert not serializer.data["changelog_short"] == expected

    def test_permissions(self, version):
        serializer = VersionSerializer(instance=version)
        assert serializer.data["permissions"] == {
            "this:delete": False,
            "this:edit": False,
        }


@pytest.mark.django_db
class TestAttachedFileSerializer:
    def test_name(self, attached_file):
        serializer = AttachedFileSerializer(instance=attached_file)
        assert serializer.data["name"].startswith("The_Game-v0.1.0-")
