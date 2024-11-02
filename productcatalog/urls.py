from django.urls import path
from . import views

urlpatterns = [
    path('', views.foo_product_catalog, name='product_catalog'),
    path('<slug:category_slug>/', views.foo_product_catalog, name='category_product_catalog'),
]
