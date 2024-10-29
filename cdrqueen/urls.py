"""
URL configuration for cdrqueen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admindashboard/', include('admindashboard.urls')),
    path('checkout/', include('checkout.urls')),
    path('helpandsupport/', include('helpandsupport.urls')),    
    path('home/', include('home.urls')),    
    path('orderhistoy/', include('orderhistory.urls')),
    path('ordermanagement/', include('ordermanagement.urls')),
    path('paymentmanagement/', include('paymentmanagement.urls')),
    path('productcatalog/', include('productcatalog.urls')),
    path('catalog/', include('productcatalog.urls')), 
    path('productdetail/', include('productdetail.urls')),
    path('productmanagement/', include('productmanagement.urls')),
    path('shippingmanagement/', include('shippingmanagement.urls')),
    path('shoppingcart/', include('shoppingcart.urls')),
    path('userauth/', include('userauth.urls')),
]
