from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_product_catalog, name='product_catalog')
]
