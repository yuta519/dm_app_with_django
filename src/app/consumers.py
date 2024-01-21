import asyncio
import json

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from app.models import Conversation, Message, User


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

        user_instance, conversation = await asyncio.gather(
            self.get_user(user["id"]), self.get_conversation(self.room_id)
        )
        await self.credate_message(user_instance, conversation, message)
        await self.send(text_data=json.dumps({"message": message, "user": user}))

    @database_sync_to_async
    def get_user(self, user_id):
        return User.objects.get(id=user_id)

    @database_sync_to_async
    def get_conversation(self, id):
        return Conversation.objects.get(id=id)

    @database_sync_to_async
    def credate_message(self, user, conversation, content):
        if not len(content):
            raise ValueError("Text is empty")
        message = Message.objects.create(
            user=user, conversation=conversation, content=content
        )
        message.save()
