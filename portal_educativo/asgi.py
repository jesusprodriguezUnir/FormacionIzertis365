"""
ASGI config for portal_educativo project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_educativo.settings')

application = get_asgi_application()
