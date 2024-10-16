from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup_page(request):  # register
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('home')  # Redirect to a homepage or another page
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', { "form": form })


def login_page(request): # Login
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', { "form": form})


