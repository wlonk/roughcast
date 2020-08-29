from django.db import models
from hashid_field import HashidAutoField

from .slugs import CustomSlugField, slugify


class BasicModelMixin(models.Model):
    class Meta:
        abstract = True

    id = HashidAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)


class SimpleSlugMixin(models.Model):
    class Meta:
        abstract = True

    slug = CustomSlugField(max_length=255, blank=True)
    slug_field_name = "name"

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(getattr(self, self.slug_field_name))
        super().save(*args, **kwargs)


class SubscribableMixin:
    def save(self, *args, **kwargs):
        try:
            self.subscribable
        except self.__class__.subscribable.RelatedObjectDoesNotExist:
            from .models import Subscribable

            self.subscribable = Subscribable.objects.create()
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        subscribable = self.subscribable
        ret = super().delete(*args, **kwargs)
        subscribable.delete()
        return ret
