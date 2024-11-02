from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'profile.html')

def address(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'address.html')

def bank_and_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'bank_and_cards.html')
