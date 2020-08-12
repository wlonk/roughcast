import re
from unittest.mock import MagicMock

import pytest

from roughcast.models import attached_file_upload_to, is_emoji


def test_attached_file_upload_to():
    instance = MagicMock(
        **{
            "version.game.publisher.name": "publisher",
            "version.game.name": "game",
            "version.name": "version",
        }
    )
    filename = "test.pdf"
    actual = attached_file_upload_to(instance, filename)
    expected = r"publisher/game/game-version-[A-Za-z0-9]{8}.pdf"
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
class TestPublisher:
    def test_str(self, publisher):
        assert str(publisher) == "Transneptune Games"


@pytest.mark.django_db
class TestPublisherMembership:
    def test_str(self, publisher_membership):
        username = publisher_membership.user.username
        assert (
            str(publisher_membership) == f"{username} is a member of Transneptune Games"
        )


@pytest.mark.django_db
class TestGame:
    def test_str(self, game):
        assert str(game) == "The Game by Transneptune Games"


@pytest.mark.django_db
class TestVersion:
    def test_str(self, version):
        assert str(version) == "The Game by Transneptune Games version v0.1.0"
