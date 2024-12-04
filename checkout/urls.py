from django.urls import path
from . import views  # Ensure this imports views from the current app

urlpatterns = [
    path('', views.checkout_view, name='checkout'),
    path('payment/', views.payment_view, name='payment'),
    path('confirm_order/', views.confirm_order_view, name='confirm_order'),  # Use `views.confirm_order_view` here
]
