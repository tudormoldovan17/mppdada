import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import car
from car import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.py')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            car.routing.websocket_urlpatterns  # Point it to your app's routing
        )
    ),
})