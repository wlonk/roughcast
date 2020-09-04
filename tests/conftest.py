import factory
import pytest
from django.contrib.auth import get_user_model
from pytest_factoryboy import register
from rest_framework.test import APIClient

from roughcast.models import (
    AlphaTestEmail,
    AttachedFile,
    Game,
    InAppNotification,
    Subscription,
    Team,
    TeamMembership,
    Version,
)

User = get_user_model()


# @TODO: Remove when out of Alpha:
@register
class AlphaTestEmailFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AlphaTestEmail

    email = factory.Sequence("user_{}@example.com".format)


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence("user_{}@example.com".format)
    username = factory.Sequence("user_{}".format)
    first_name = "Alex Rodriguez"


@register
class SubscriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscription

    user = factory.SubFactory(UserFactory)


@register
class TeamFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Team

    name = "Transneptune Games"
    slug = "transneptune-games"


@register
class TeamMembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TeamMembership

    user = factory.SubFactory(UserFactory)
    team = factory.SubFactory(TeamFactory)
    is_owner = False


@register
class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    team = factory.SubFactory(TeamFactory)
    name = "The Game"
    slug = "the-game"


@register
class VersionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Version

    game = factory.SubFactory(GameFactory)
    name = "v0.1.0"
    slug = "v0.1.0"
    created_by = factory.SubFactory(UserFactory)


@register
class AttachedFileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AttachedFile

    version = factory.SubFactory(VersionFactory)
    attached_file = factory.django.FileField()


@register
class InAppNotificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InAppNotification

    user = factory.SubFactory(UserFactory)
    notification_type = "comments"
    path = "/test/path"


@pytest.fixture
def client(user_factory):
    user = user_factory()
    token = user.get_or_create_token()
    client = APIClient(HTTP_AUTHORIZATION=f"Token {token}")
    client.force_login(user)
    client.user = user
    return client
