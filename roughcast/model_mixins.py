from django.db import models
from django.utils.text import slugify
from hashid_field import HashidAutoField


class BasicModelMixin(models.Model):
    class Meta:
        abstract = True

    id = HashidAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)


class SimpleSlugMixin(models.Model):
    class Meta:
        abstract = True

    slug = models.SlugField(max_length=255, blank=True, unique=True)
    slug_field_name = "name"

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(getattr(self, self.slug_field_name))
        super().save(*args, **kwargs)
