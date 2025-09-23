from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('create/', views.create_item, name='create_item'),  # <- aquí es donde carga su producto
]

# {% url 'item_list' %} → redirige a la lista de productos (tu “inicio” real del marketplace).