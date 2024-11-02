from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_checkout(request):
    return HttpResponse("Welcome to Checkout!")
