from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_payment_management, name='Payment Management')
]
