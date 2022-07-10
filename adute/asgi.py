import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adute.settings')

asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": asgi_app,
    # Just HTTP for now. (We can add other protocols later.)
})