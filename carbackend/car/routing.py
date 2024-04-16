from channels.generic.websocket import AsyncWebsocketConsumer
from rest_framework.utils import json
from django.urls import path
import consumers

from car.serializers import CarSerializer


class CarConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass # Not always necessary

    async def receive(self, text_data):
        # You would trigger this by saving a new car entry to the database.
        # ... your logic to retrieve the new car ...
        await self.send(text_data=json.dumps({
            'type': 'car_added',
            'car': CarSerializer  # Serialize your new car data
        }))



websocket_urlpatterns = [
    path('ws/cars/', CarConsumer.as_asgi()),
]