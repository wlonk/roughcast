from functools import reduce

from rest_framework import serializers
from rest_framework.fields import SlugField as BaseSlugField

from .models import NotificationPreferences, User
from .slugs import validate_slug


class UserStringField(serializers.RelatedField):
    def to_internal_value(self, data):
        return User.objects.get(username=data)

    def to_representation(self, value):
        return value.username


class SlugStringField(serializers.RelatedField):
    def __init__(self, *args, model_class, **kwargs):
        self.model_class = model_class
        return super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        return self.model_class.objects.get(slug=data)

    def to_representation(self, value):
        return value.slug


class SlugField(BaseSlugField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [validate_slug]


class NotificationMaskField(serializers.Field):
    def to_representation(self, value):
        """Makes something JSONable out of a Python object"""
        return {
            name.lower(): bool(member & value)
            for name, member in NotificationPreferences.__members__.items()
            if member != NotificationPreferences.NONE
        }

    def to_internal_value(self, data):
        """Makes a Python object out of something JSONable"""
        vals = [
            NotificationPreferences[key.upper()] for key, val in data.items() if val
        ]
        mask = reduce(lambda a, b: a | b, vals, NotificationPreferences.NONE)
        return mask


class SubscriptionModelInstanceField(serializers.Field):
    # TODO: validate.
    def _try_get_subscribable_model(self, subscribable):
        # These are lower-case to match the model attributes:
        for model_name in ("team", "game"):
            exceptions = (
                getattr(subscribable.__class__, model_name).RelatedObjectDoesNotExist,
            )
            try:
                return getattr(subscribable, model_name)
            except exceptions:
                pass

    def to_representation(self, value):
        subscribable_model = self._try_get_subscribable_model(value)
        return f"{subscribable_model.__class__.__name__}:{subscribable_model.id}"

    def to_internal_value(self, data):
        from .models import Game, Team

        model_name, id_ = data.split(":")
        model_class = {
            "Team": Team,
            "Game": Game,
        }[model_name]
        instance = model_class.objects.get(pk=id_)
        return instance
