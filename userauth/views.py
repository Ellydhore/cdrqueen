from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_user_auth(request):
    return HttpResponse("Welcome to User Authentication!")

def registerPage(request):
    context = {}
    return render(request, 'template/signup.html', context)

def loginPage(request):
    context = {}
    return render(request, 'template/login.html', context)


