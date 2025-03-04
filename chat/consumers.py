import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join the room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Send all previous messages
        messages = await sync_to_async(lambda: list(Message.objects.all()))()
        for message in messages:
            await self.send(text_data=json.dumps({"message": message.content}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data["message"]

        # Save message to the database
        message = await sync_to_async(Message.objects.create)(content=message_content)

        # Broadcast the message to all clients in the room
        await self.channel_layer.group_send(self.room_group_name, {"type": "chat.message", "message": message.content})

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({"message": event["message"]}))
