import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Car  # Import your Car model
from .serializers import CarSerializer  # And the serializer


class CarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("cars", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("cars", self.channel_name)

    async def car_added(self, event):
        # This method is called when a new car is added
        new_car = event['car']  # Assuming serializer data is in 'car' key
        await self.send(text_data=json.dumps(new_car))