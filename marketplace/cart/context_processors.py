# cart/context_processors.py
from .models import Cart, CartItem
from .utils import EXCHANGE_RATES

def currency_context(request):
    currency = request.session.get('currency', 'USD')  # moneda por defecto
    return {
        'current_currency': currency,
        'available_currencies': EXCHANGE_RATES.keys()
    }

def cart_info(request):
    """
    Context processor para mostrar información del carrito
    en todas las plantillas.
    Variables disponibles:
        - cart_subtotal: total del carrito
        - cart_items_count: cantidad total de productos (sumando cantidades)
    """
    total = 0
    count = 0

    if request.user.is_authenticated:
        try:
            # Obtener el carrito del usuario
            cart = Cart.objects.get(user=request.user)
            items = CartItem.objects.filter(cart=cart)

            # Calcular subtotal
            total = sum([item.get_subtotal for item in items])

            # Contar cantidad total de productos
            count = sum([item.quantity for item in items])

        except Cart.DoesNotExist:
            # Si no hay carrito creado
            total = 0
            count = 0

    return {
        'cart_subtotal': total,
        'cart_items_count': count
    }
