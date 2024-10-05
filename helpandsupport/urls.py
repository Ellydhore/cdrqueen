from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_help_and_support, name='help_and_support')
]
