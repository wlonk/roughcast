import pytest
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.text import slugify

from roughcast.email_verification import _get_activation_key


@pytest.mark.django_db
class TestAccountsView:
    def test_list(self, client):
        response = client.get("/api/accounts/")
        expected = {
            "login": "http://testserver/api/accounts/login/",
            "profile": "http://testserver/api/accounts/profile/",
            "register": "http://testserver/api/accounts/register/",
            "reset_password": "http://testserver/api/accounts/reset_password/",
            "reset_password_confirm": (
                "http://testserver/api/accounts/reset_password_confirm/"
            ),
            "verify_email": "http://testserver/api/accounts/verify_email/",
            "request_verify_email": (
                "http://testserver/api/accounts/request_verify_email/"
            ),
        }
        assert response.json() == expected


@pytest.mark.django_db
class TestRegisterView:
    def test_serializer_errors(self, client):
        response = client.post("/api/accounts/register/")
        assert response.status_code == 400
        assert response.json() == {
            "username": ["This field is required."],
            "email": ["This field is required."],
            "password1": ["This field is required."],
            "password2": ["This field is required."],
            "tos": ["This field is required."],
        }

    def test_good(self, client, alpha_test_email_factory):
        alpha_test_email_factory(email="test@example.com")
        data = {
            "username": "test_user",
            "email": "test@example.com",
            "password1": "bar12foo",
            "password2": "bar12foo",
            "tos": True,
        }
        response = client.post("/api/accounts/register/", data)
        assert response.status_code == 201, response.json()
        assert response.json()["username"] == "test_user"


@pytest.mark.django_db
class TestLoginView:
    def test_serializer_errors(self, client):
        response = client.post("/api/accounts/login/")
        assert response.status_code == 400
        assert response.json() == {
            "username": ["This field is required."],
            "password": ["This field is required."],
        }

    def test_invalid_credentials_no_user(self, client, user_factory):
        user = user_factory(username="testorr")
        user.set_password("foobar")
        user.save()
        data = {
            "username": "rrotset",
            "password": "barfoo",
        }
        response = client.post("/api/accounts/login/", data)
        assert response.status_code == 400
        assert response.json() == {
            "non_field_errors": ["Invalid credentials."],
        }

    def test_invalid_credentials(self, client, user_factory):
        user = user_factory(username="testorr")
        user.set_password("foobar")
        user.save()
        data = {
            "username": "testorr",
            "password": "barfoo",
        }
        response = client.post("/api/accounts/login/", data)
        assert response.status_code == 400
        assert response.json() == {
            "non_field_errors": ["Invalid credentials."],
        }

    def test_good(self, client, user_factory):
        user = user_factory(username="testorr")
        user.set_password("foobar")
        user.save()
        data = {
            "username": "testorr",
            "password": "foobar",
        }
        response = client.post("/api/accounts/login/", data)
        assert response.status_code == 200
        assert response.json()["username"] == "testorr"
        assert response.json()["token"] != ""


@pytest.mark.django_db
class TestUserViewSet:
    def test_list(self, user, client):
        response = client.get("/api/users/")
        assert response.status_code == 200
        assert len(response.json()) > 0

    def test_detail__other(self, user, client):
        response = client.get(f"/api/users/{user.username}/")
        assert response.status_code == 200
        assert response.json()["username"] == user.username

    def test_me(self, client):
        response = client.get("/api/users/me/")
        assert response.status_code == 200
        assert response.json()["username"] == client.user.username

    def test_profile__get(self, client):
        response = client.get("/api/accounts/profile/")
        assert response.status_code == 200

    def test_profile__put__bad(self, client):
        data = {}
        response = client.put("/api/accounts/profile/", data, format="json")
        assert response.status_code == 400

    def test_profile__put__good(self, client):
        data = {
            "notif_comments": {
                "in_app": True,
                "instant_email": True,
                "digest_email": False,
            },
            "notif_mentions": {
                "in_app": True,
                "instant_email": True,
                "digest_email": False,
            },
            "notif_versions": {
                "in_app": True,
                "instant_email": True,
                "digest_email": False,
            },
            "notif_games": {
                "in_app": True,
                "instant_email": True,
                "digest_email": False,
            },
        }
        response = client.put("/api/accounts/profile/", data, format="json")
        assert response.status_code == 200

    def test_verify_email__invalid(self, client):
        response = client.post("/api/accounts/verify_email/")
        assert response.status_code == 400

    def test_verify_email__error(self, client):
        data = {"key": "bad key"}
        response = client.post("/api/accounts/verify_email/", data)
        assert response.status_code == 400

    def test_verify_email__good(self, client):
        key = _get_activation_key(client.user)
        data = {"key": key}
        response = client.post("/api/accounts/verify_email/", data)
        assert response.status_code == 204

    def test_request_verify_email(self, client):
        response = client.post("/api/accounts/request_verify_email/")
        assert response.status_code == 202

    def test_reset_password__invalid(self, client):
        response = client.post("/api/accounts/reset_password/")
        assert response.status_code == 400

    def test_reset_password__good(self, client):
        data = {"email": "test@example.com"}
        response = client.post("/api/accounts/reset_password/", data)
        assert response.status_code == 202

    def test_reset_password_confirm__invalid(self, client):
        response = client.post("/api/accounts/reset_password_confirm/")
        assert response.status_code == 400

    def test_reset_password_confirm__good(self, client):
        uid = urlsafe_base64_encode(force_bytes(client.user.pk))
        token = default_token_generator.make_token(client.user)
        data = {
            "uid": uid,
            "token": token,
            "password1": "bar12foo",
            "password2": "bar12foo",
        }
        response = client.post("/api/accounts/reset_password_confirm/", data)
        assert response.status_code == 204


@pytest.mark.django_db
class TestTeamInviteViewSet:
    def test_queryset(self, client):
        response = client.get("/api/invites/")
        assert len(response.json()) == 0

    def test_accept__bad(self, client, team_membership_factory, team_invite_factory):
        membership = team_membership_factory(user=client.user)
        invite = team_invite_factory(team=membership.team)
        response = client.post(f"/api/invites/{invite.pk}/accept/")
        assert response.status_code == 403

    def test_accept__good(self, client, team_invite_factory):
        invite = team_invite_factory(to_email=client.user.email)
        response = client.post(f"/api/invites/{invite.pk}/accept/")
        assert response.status_code == 201


@pytest.mark.django_db
class TestSubscriptionViewSet:
    def test_queryset(self, client):
        response = client.get("/api/subscriptions/")
        assert len(response.json()) == 0


@pytest.mark.django_db
class TestInAppNotificationViewSet:
    def test_queryset(self, client, in_app_notification_factory):
        notif = in_app_notification_factory(user=client.user)
        in_app_notification_factory()
        response = client.get("/api/notifications/")
        assert len(response.json()) == 1
        assert response.json()[0]["id"] == str(notif.id)


@pytest.mark.django_db
class TestVersionViewSet:
    def test_queryset_anonymous(self, anon_client, version_factory):
        version = version_factory(is_public=True)
        version_factory(is_public=False)
        response = anon_client.get("/api/versions/")
        assert len(response.json()) == 1
        assert version.id in [v["id"] for v in response.json()]

    def test_archive_link(self, client, version, attached_file_factory):
        attached_file_factory(version=version)
        response = client.get(f"/api/versions/{version.id}/archive/")
        filename = slugify(f"{version.game.name} {version.name}")
        assert (
            response.get("Content-Disposition")
            == f"attachment; filename={filename}.zip"
        )
