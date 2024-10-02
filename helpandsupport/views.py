from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_help_and_support(request):
    return HttpResponse("Welcome to Help and Support!")
