from django.db import models
from django.contrib.auth.models import User
from item.models import Item
from django.utils import timezone


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona el carrito con un usuario
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Carrito de {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.item.name}"
    
    # Método para obtener el subtotal
    @property
    def get_subtotal(self):
        return self.item.price * self.quantity
