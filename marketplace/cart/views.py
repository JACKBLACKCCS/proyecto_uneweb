from django.shortcuts import render, redirect, get_object_or_404 
from .models import Cart, CartItem
from item.models import Item
from django.contrib.auth.decorators import login_required

# -------------------------------------------------------------------
# 📌 BLOQUE CRUD DEL CARRITO
# -------------------------------------------------------------------

# READ - Ver el carrito y los productos que contiene
@login_required(login_url='/accounts/login/')
def view_cart(request):
    # Obtiene o crea un carrito asociado al usuario
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    # Calcula el subtotal de cada producto (precio x cantidad)
    for item in items:
        item.subtotal = item.get_subtotal  

    # Calcula el total de la compra sumando todos los subtotales
    total = sum(item.subtotal for item in items)

    # Pasa los datos a la plantilla
    context = {
        'items': items,
        'total': total
    }
    return render(request, 'cart/view_cart.html', context)


# CREATE - Agregar un producto al carrito
@login_required(login_url='/accounts/login/')
def add_to_cart(request, item_id):
    cart, created = Cart.objects.get_or_create(user=request.user)
    item = get_object_or_404(Item, id=item_id)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    # Si ya existía en el carrito, aumenta la cantidad
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')


# DELETE - Eliminar un producto del carrito
@login_required(login_url='/accounts/login/')
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    cart_item.delete()  # Elimina el producto del carrito
    return redirect('view_cart')


# UPDATE - Aumentar cantidad de un producto
@login_required(login_url='/accounts/login/')
def increase_quantity(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')


# UPDATE - Disminuir cantidad de un producto
@login_required(login_url='/accounts/login/')
def decrease_quantity(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)

    if cart_item.quantity > 1:
        # Si hay más de uno, simplemente resta 1
        cart_item.quantity -= 1
        cart_item.save()
    else:
        # Si solo queda 1 y se resta, el producto se elimina del carrito
        cart_item.delete()
    
    return redirect('view_cart')



#  CHECKOUT inicio

# Checkout (pago)
@login_required(login_url='/accounts/login/')
def checkout(request):
    # Obtener el carrito del usuario
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    # Calcular subtotal para cada item
    for item in items:
        item.subtotal = item.get_subtotal  

    # Calcular total
    total = sum(item.subtotal for item in items)

    context = {
        'items': items,
        'total': total
    }

    return render(request, 'cart/checkout.html', context)
