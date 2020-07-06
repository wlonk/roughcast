from rest_framework import serializers

from .models import User


class UserStringField(serializers.RelatedField):
    def to_internal_value(self, data):
        return User.objects.get(username=data)

    def to_representation(self, value):
        return str(value)


class SlugStringField(serializers.RelatedField):
    def __init__(self, *args, model_class, **kwargs):
        self.model_class = model_class
        return super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        return self.model_class.objects.get(slug=data)

    def to_representation(self, value):
        return value.slug
