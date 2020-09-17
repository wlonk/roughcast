# @@@ WEBSOCKETS
# from channels.generic.websocket import AsyncJsonWebsocketConsumer
# from .ws_serializers import SubscriptionSerializer


# class PushNotificationConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#     # De facto, this is "subscribe" and "unsubscribe":
#     async def receive_json(self, content, **kwargs):
#         serializer = SubscriptionSerializer(content)
#         if not serializer.is_valid():
#             await self.send_json(serializer.errors)
#             return

#         group_name = serializer.get_group_name()
#         self.groups.append(group_name)

#         if serializer.is_subscribe():
#             await self.channel_layer.group_add(group_name, self.channel_name)
#             await self.send_json(serializer.subscribe_message())

#         if serializer.is_unsubscribe():
#             await self.send_json(serializer.unsubscribe_message())
#             await self.channel_layer.group_discard(group_name, self.channel_name)

#     async def notify(self, event):
#         """
#         Handler for calls like::

#             channel_layer.group_send(group_name, {
#                 'type': 'notify',  # This routes it to this handler.
#                 'content': {
#                     # Will map to a frontend Vuex action:
#                     'type': str,
#                     # Serialized representation of the new data:
#                     'payload': obj,
#                     # The resource that this pertains to (also the path
#                     # you could query in the REST API to get this
#                     # entity):
#                     "resource_identifier": str,
#                     # When this event was queued (so that out-of-order
#                     # ones can be ignored):
#                     "timestamp": datetime,
#                 },
#             })
#         """
#         if "content" in event:
#             await self.send_json(event["content"])
