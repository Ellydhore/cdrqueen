from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_order_history, name='order_history')
]
