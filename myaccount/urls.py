from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('add_address/', views.add_address, name='add_address'),
    path('address/delete_address/<int:address_id>/', views.delete_address, name='delete_address'),
    path('address/set-default-address/<int:address_id>/', views.set_default_address, name='set_default_address'),
    path('bank_and_cards/', views.bank_and_cards, name='bank_and_cards')
]
