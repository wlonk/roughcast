# @@@ WEBSOCKETS
# from rest_framework import serializers


# class SubscriptionSerializer(serializers.Serializer):
#     SUBSCRIBE = "subscribe"
#     UNSUBSCRIBE = "unsubscribe"

#     action = serializers.ChoiceField(choices=(SUBSCRIBE, UNSUBSCRIBE))
#     resource_identifier = serializers.CharField()

#     def validate_resource_identifier(self, value):
#         # We cannot access the database here without wrapping it in
#         # channels.db.database_sync_to_async. We may eventually do that,
#         # but for now, we are hard-coding the one acceptable resource:
#         # `notifications/`.
#         if value != "notifications/":
#             raise serializers.ValidationError(f"Resource {value!r} not allowed.")
#         return value

#     def get_group_name(self):
#         return self.validated_data["resource_identifier"]

#     def is_subscribe(self):
#         return self.validated_data["action"] == SUBSCRIBE

#     def is_unsubscribe(self):
#         return self.validated_data["action"] == UNSUBSCRIBE

#     def subscribe_message(self):
#         resource_identifier = self.validated_data["resource_identifier"]
#         return {"ok": f"Subscribed to {resource_identifier}"}

#     def unsubscribe_message(self):
#         resource_identifier = self.validated_data["resource_identifier"]
#         return {"ok": f"Unsubscribed to {resource_identifier}"}
