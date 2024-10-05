from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_product_detail, name='product_detail')
]
