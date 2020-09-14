import pytest

from roughcast.models import Team, User
from roughcast.serializer_fields import (
    NotificationMaskField,
    SlugStringField,
    UserStringField,
)


@pytest.mark.django_db
class TestUserStringField:
    def test_to_internal_value(self, user):
        assert (
            UserStringField(queryset=User.objects.all()).to_internal_value(
                user.username
            )
            == user
        )

    def test_to_representation(self, user):
        assert (
            UserStringField(queryset=User.objects.all()).to_representation(user)
            == user.username
        )


@pytest.mark.django_db
class TestSlugStringField:
    def test_to_internal_value(self, team):
        assert (
            SlugStringField(
                model_class=Team, queryset=Team.objects.all()
            ).to_internal_value(team.slug)
            == team
        )

    def test_to_representation(self, team):
        assert (
            SlugStringField(
                model_class=Team,
                queryset=Team.objects.all(),
            ).to_representation(team)
            == team.slug
        )


class TestNotificationMaskField:
    @pytest.mark.parametrize(
        "data,expected",
        [
            ({"in_app": False, "instant_email": False, "digest_email": False}, 0),
            ({"in_app": True, "instant_email": False, "digest_email": False}, 1),
            ({"in_app": False, "instant_email": True, "digest_email": False}, 2),
            ({"in_app": True, "instant_email": True, "digest_email": False}, 3),
            ({"in_app": False, "instant_email": False, "digest_email": True}, 4),
            ({"in_app": True, "instant_email": False, "digest_email": True}, 5),
            ({"in_app": False, "instant_email": True, "digest_email": True}, 6),
            ({"in_app": True, "instant_email": True, "digest_email": True}, 7),
        ],
    )
    def test_to_internal_value(self, data, expected):
        assert NotificationMaskField().to_internal_value(data) == expected

    @pytest.mark.parametrize(
        "mask,expected",
        [
            (0, {"in_app": False, "instant_email": False, "digest_email": False}),
            (1, {"in_app": True, "instant_email": False, "digest_email": False}),
            (2, {"in_app": False, "instant_email": True, "digest_email": False}),
            (3, {"in_app": True, "instant_email": True, "digest_email": False}),
            (4, {"in_app": False, "instant_email": False, "digest_email": True}),
            (5, {"in_app": True, "instant_email": False, "digest_email": True}),
            (6, {"in_app": False, "instant_email": True, "digest_email": True}),
            (7, {"in_app": True, "instant_email": True, "digest_email": True}),
        ],
    )
    def test_to_representation(self, mask, expected):
        assert NotificationMaskField().to_representation(mask) == expected
