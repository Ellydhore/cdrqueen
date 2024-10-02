from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_order_management, name='Order Management')
]
