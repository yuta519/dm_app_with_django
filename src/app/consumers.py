import json

from channels.generic.websocket import AsyncWebsocketConsumer

# TODO: Will save messages to database
# from app.models import Conversation, Message


class ChatConsumer(AsyncWebsocketConsumer):
    room_id = None

    async def connect(self):
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]
        await self.channel_layer.group_add(self.room_id, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_id, self.channel_layer)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        await self.channel_layer.group_send(
            self.room_id,
            {
                "type": "sendMessage",
                "message": message,
                "user": user,
            },
        )

    async def sendMessage(self, event):
        message = event["message"]
        user = event["user"]
        await self.send(text_data=json.dumps({"message": message, "user": user}))
