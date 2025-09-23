from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = "Crea un superusuario si no existe (para Render)"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

        if not username or not email or not password:
            self.stdout.write(self.style.ERROR("❌ Faltan variables de entorno para superusuario"))
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f"✅ Superuser '{username}' creado"))
        else:
            self.stdout.write(self.style.WARNING(f"⚠️ Superuser '{username}' ya existe"))


