# @@@ WEBSOCKETS
# from asgiref.sync import async_to_sync
# from channels.layers import get_channel_layer
# from django.utils import timezone
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


# @@@ WEBSOCKETs
# class PushableMixin:
#     # Subclasses implement these:
#     push_resource = None
#     push_serializer = None

#     @staticmethod
#     def _json_format_timestamp(value):
#         value = value.isoformat()
#         if value.endswith('+00:00'):
#             value = value[:-6] + 'Z'
#         return value

#     def push(self):
#         channel_layer = get_channel_layer()

#         # @@@ If we eventually enable subscribing to individual models,
#         # this will have to support translating between `foo/:id/`
#         # format and `foo/` format, for details and collections.
#         group_name = self.push_resource
#         timestamp = self._json_format_timestamp(timezone.now())

#         message = {
#             # TODO: make this line right:
#             "type": "getPushNotification",
#             "payload": self.push_serializer(instance=self).data,
#             "resource_identifier": f"{self.push_resource}/{self.id}/",
#             "timestamp": datetime,
#         }

#         sent_message = {"type": "notify", "content": message}
#         async_to_sync(channel_layer.group_send)(group_name, sent_message)

#     def save(self, *args, **kwargs):
#         is_created = not self.id
#         ret = super().save(*args, **kwargs)
#         if is_created:
#             self.push()

#         return ret
