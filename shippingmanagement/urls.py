from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_shipping_management, name='shipping_management')
]
