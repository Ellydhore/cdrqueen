from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_product_catalog(request):
    return HttpResponse("Welcome to Product Catalog!")