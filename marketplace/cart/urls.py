from django.urls import path
from . import views

urlpatterns = [
  # Crud del carrito =

 # READ - Ver carrito :
    path('view/', views.view_cart, name='view_cart'),

 # CREATE - Agregar producto al carrito
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),

 # DELETE - Eliminar producto del carrito
    path('remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),

 # UPDATE - Aumentar cantidad
    path('increase/<int:item_id>/', views.increase_quantity, name='cart_increase'),

 # UPDATE - Disminuir cantidad
    path('decrease/<int:item_id>/', views.decrease_quantity, name='cart_decrease'),

 #  CHECKOUT (Pago)
    path('checkout/', views.checkout, name='checkout'),

    ]