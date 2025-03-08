import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.models import Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # if self.scope["user"].is_anonymous:
        #     await self.close()  # Reject connection if user is not authenticated
        #     return

        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        _room = await sync_to_async(lambda: Room.objects.filter(name=self.room_name).first())()
        if not _room:
            await self.close()
            return

        # Join the room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Send all previous messages
        messages = await sync_to_async(lambda: list(Message.objects.all().select_related("author")))()
        for message in messages:
            await self.send(
                text_data=json.dumps(
                    {
                        "message": message.content,
                        "user": message.author.username,
                        "avatar": str(message.author.avatar),
                        "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                    }
                )
            )

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # if self.scope["user"].is_anonymous:
        # return  # Ignore messages from unauthenticated users
        data = json.loads(text_data)
        message_content = data["message"]

        # Save message to the database
        message = await sync_to_async(Message.objects.create)(
            content=message_content, author=self.scope["user"]
        )

        # Broadcast the message to all clients in the room
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "message": message.content,
                "user": message.author.username,
                "avatar": str(message.author.avatar),
                "created_at": message.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {"message": event["message"], "user": event["user"], "avatar": event["avatar"]}
            )
        )
