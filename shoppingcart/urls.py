from django.urls import path
from . import views

urlpatterns = [
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),  
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
