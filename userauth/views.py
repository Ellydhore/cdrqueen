from django.shortcuts import render, HttpResponse

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')
