from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartItem
from item.models import Item
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

def set_currency(request, currency_code):
    request.session['currency'] = currency_code
    return redirect(request.META.get('HTTP_REFERER', '/'))

# Función para ver el carrito
@login_required(login_url='/accounts/login/')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    # Calcular subtotal para cada item usando el método del modelo
    for item in items:
        item.subtotal = item.get_subtotal  # usando el property del modelo

    # Calcular total del carrito
    total = sum(item.subtotal for item in items)

    context = {
        'items': items,
        'total': total
    }
    return render(request, 'cart/view_cart.html', context)

# Función para agregar un item al carrito
@login_required(login_url='/accounts/login/')
def add_to_cart(request, item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('view_cart')

# Función para eliminar un item del carrito
@login_required(login_url='/accounts/login/')
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    cart_item.delete()
    return redirect('view_cart')

# Función para aumentar cantidad
@login_required(login_url='/accounts/login/')
def increase_quantity(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

# Función para disminuir cantidad
@login_required(login_url='/accounts/login/')
def decrease_quantity(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()  # Si llega a 0, se elimina del carrito
    return redirect('view_cart')

