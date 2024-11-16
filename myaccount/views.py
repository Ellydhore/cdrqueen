from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from .forms import ProfileForm, AddressForm
from usermanagement.models import Address

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

    user = request.user
    addresses = Address.objects.filter(user=user)  # Get all addresses for the user
    
    return render(request, 'address.html', {'addresses': addresses})

def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user  # Assuming Address has a ForeignKey to User
            address.save()
            return redirect('address')  # Redirect to the address page after saving
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({'message': 'Invalid request'}, status=400)

def bank_and_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'bank_and_cards.html')

