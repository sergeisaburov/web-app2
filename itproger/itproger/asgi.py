"""
обеспечивает корректеное подключение к серверу,(выгрузка сайта)
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'itproger.settings')

application = get_asgi_application()
