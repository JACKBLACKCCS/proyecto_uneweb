"""
WSGI config for marketplace project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys

# Agrega la ruta de tu proyecto
path = '/home/MoisesV/proyecto_uneweb/marketplace'
if path not in sys.path:
    sys.path.append(path)

# Configura el settings module de Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'marketplace.settings'

# Importa y configura la aplicación Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()