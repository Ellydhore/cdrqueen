from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_shopping_cart, name='shopping_cart')
]
