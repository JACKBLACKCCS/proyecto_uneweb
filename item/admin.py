# item/admin.py
from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    # Excluir los campos de fecha/hora
    exclude = ('created_at', 'updated_at')  # ← Añade esta línea
    # Si tienes otros campos de timestamp, añádelos aquí también

admin.site.register(Item, ItemAdmin)  # ← Registra con la clase personalizada
