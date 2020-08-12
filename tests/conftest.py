import factory
import pytest
from django.contrib.auth import get_user_model
from pytest_factoryboy import register
from rest_framework.test import APIClient

from roughcast.models import (
    Publisher,
    PublisherMembership,
    Game,
    Version,
)

User = get_user_model()


@register
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence("user_{}@example.com".format)
    username = factory.Sequence("user_{}".format)
    first_name = "Alex Rodriguez"
    password = factory.PostGenerationMethodCall("set_password", "foobar")


@register
class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = "Transneptune Games"
    slug = "transneptune-games"


@register
class PublisherMembershipFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PublisherMembership

    user = factory.SubFactory(UserFactory)
    publisher = factory.SubFactory(PublisherFactory)
    is_owner = False


@register
class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    publisher = factory.SubFactory(PublisherFactory)
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


@pytest.fixture
def client(user_factory):
    user = user_factory()
    client = APIClient()
    client.force_login(user)
    client.user = user
    return client
