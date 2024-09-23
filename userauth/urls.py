from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_user_auth, name='User Authentication')
]
