from django.urls import path
from . import views

urlpatterns = [
    path('to-recieve/', views.to_recieve, name='to_recieve')
]
