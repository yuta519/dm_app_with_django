import json

from channels.generic.websocket import AsyncWebsocketConsumer

# TODO: Will save messages to database
# from app.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    room_name = None

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_layer)

    async def receive(self, received_data):
        data = json.loads(received_data)
        message, user = data["message"], data["user"]
        await self.channel_layer.group_send(
            self.room_name, {"message": message, "user": user}
        )

    async def sendMessage(self, event):
        message = event["message"]
        user = event["user"]
        await self.send(text_data=json.dumps({"message": message, "user": user}))
