# create_superuser.py - CON TUS DATOS REALES
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    
    # ⚠️ REEMPLAZA CON TUS DATOS REALES ⚠️
    if not User.objects.filter(username='jackblack').exists():  # Tu usuario real
        User.objects.create_superuser(
            username='Moises',                    # Tu usuario preferido
            email='velll@gmail.com',          # Tu email real
            password='1121candy*'       # Password MUY seguro
        )
        print("✅ Superuser creado exitosamente!")
    else:
        print("⚠️  El superusuario ya existe.")

if __name__ == '__main__':
    create_superuser()