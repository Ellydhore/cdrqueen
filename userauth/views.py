from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_user_auth(request):
    return HttpResponse("Welcome to User Authentication!")
