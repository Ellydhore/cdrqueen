from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, "signup.html", {"form": form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember = request.POST.get("remember")
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            
            if remember:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Session expires when the browser closes
            
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('home')
