from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('bank_and_cards/', views.bank_and_cards, name='bank_and_cards')
]
