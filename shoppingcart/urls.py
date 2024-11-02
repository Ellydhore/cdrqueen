from django.urls import path
from . import views

urlpatterns = [
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),  # Access at /shopping-cart/
]
