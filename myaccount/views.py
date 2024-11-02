from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import ProfileForm

# Create your views here.
def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    formatted_phone_number = request.user.phone_number  # Initialize with the user's phone number
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form, 'formatted_phone_number': formatted_phone_number})

def address(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'address.html')

def bank_and_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'bank_and_cards.html')
