from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('view/', views.view_cart, name='view_cart'),
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='cart_remove'),
    path('increase/<int:item_id>/', views.increase_quantity, name='cart_increase'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='cart_decrease'),
    path('set_currency/<str:currency_code>/', views.set_currency, name='set_currency'),
]
