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
