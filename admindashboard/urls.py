from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_admin_dash, name='admindashboard')
]
