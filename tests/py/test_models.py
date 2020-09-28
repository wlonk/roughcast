import re
from unittest.mock import MagicMock

import pytest

from roughcast.models import (
    InAppNotification,
    NotificationPreferences,
    Subscribable,
    attached_file_upload_to,
    is_emoji,
)


def test_attached_file_upload_to():
    instance = MagicMock(
        **{
            "version.game.team.name": "team",
            "version.game.name": "game",
            "version.name": "version",
        }
    )
    filename = "test.pdf"
    actual = attached_file_upload_to(instance, filename)
    expected = r"team/game/game-version-[A-Za-z0-9]{8}.pdf"
    assert re.match(expected, actual)


def test_is_emoji():
    assert not is_emoji("x")
    assert is_emoji("🦊")


@pytest.mark.django_db
class TestUser:
    def test_str(self, user):
        assert str(user) == f"Alex Rodriguez (@{user.username})"

    def test_get_full_name(self, user):
        assert user.get_full_name() == "Alex Rodriguez"

    def test_get_or_create_token(self, user):
        assert isinstance(user.get_or_create_token(), str)


@pytest.mark.django_db
class TestUserProfile:
    def test_str(self, user):
        assert str(user.profile) == f"UserProfile for {user.username}"

    def test_should_notify(self, user):
        user.profile.notif_comments = 0
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.IN_APP
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 1
        assert user.profile._should_notify("comments", NotificationPreferences.IN_APP)
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 2
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.IN_APP
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 3
        assert user.profile._should_notify("comments", NotificationPreferences.IN_APP)
        assert user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 4
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.IN_APP
        )
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 5
        assert user.profile._should_notify("comments", NotificationPreferences.IN_APP)
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 6
        assert not user.profile._should_notify(
            "comments", NotificationPreferences.IN_APP
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )

        user.profile.notif_comments = 7
        assert user.profile._should_notify("comments", NotificationPreferences.IN_APP)
        assert user.profile._should_notify(
            "comments", NotificationPreferences.INSTANT_EMAIL
        )
        assert user.profile._should_notify(
            "comments", NotificationPreferences.DIGEST_EMAIL
        )


@pytest.mark.django_db
class TestTeam:
    def test_str(self, team):
        assert str(team) == "Team 1"

    def test_subscribable_delete(self, team_factory):
        team = team_factory()
        assert Subscribable.objects.count() == 1
        team.delete()
        assert Subscribable.objects.count() == 0


@pytest.mark.django_db
class TestTeamMembership:
    def test_str(self, team_membership):
        username = team_membership.user.username
        team_name = team_membership.team.name
        assert str(team_membership) == f"{username} is a member of {team_name}"


@pytest.mark.django_db
class TestGame:
    def test_str(self, game):
        team_name = game.team.name
        assert str(game) == f"Game 1 by {team_name}"


@pytest.mark.django_db
class TestVersion:
    def test_str(self, version):
        game_name = version.game.name
        team_name = version.game.team.name
        assert str(version) == f"{game_name} by {team_name} version v0.1.0"

    def test_notify(self, game, user, subscription_factory, version_factory):
        subscription_factory(user=user, subscribable=game.subscribable)
        assert not InAppNotification.objects.filter(user=user).exists()
        version_factory(game=game)
        assert InAppNotification.objects.filter(user=user).exists()
