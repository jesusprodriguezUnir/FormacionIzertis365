"""
WSGI config for portal_educativo project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal_educativo.settings')

application = get_wsgi_application()
