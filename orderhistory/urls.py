from django.urls import path
from . import views

urlpatterns = [
    path('all-purchases/', views.all_purchases, name='all_purchases'),
    path('cancelled/', views.cancelled, name='cancelled'),
    path('completed/', views.completed, name='completed'),
    path('return-refund/', views.return_refund, name='return_refund'),
    path('to-recieve/', views.to_recieve, name='to_recieve'),
]
