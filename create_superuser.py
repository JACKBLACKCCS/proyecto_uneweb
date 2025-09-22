# create_superuser.py - CON TUS DATOS REALES

import os
import django
from django.core.management import execute_from_command_line


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()

    USERNAME = 'Moises'  # nombre para verificar y crear
    EMAIL = 'velll@gmail.com'
    PASSWORD = '1121candy*'
    
    if not User.objects.filter(username=USERNAME).exists():
        User.objects.create_superuser(
            username=USERNAME,
            email=EMAIL,
            password=PASSWORD
        )
        print(f"✅ Superuser '{USERNAME}' creado exitosamente!")
    else:
        print(f"⚠️  El superusuario '{USERNAME}' ya existe.")

if __name__ == '__main__':
    create_superuser()