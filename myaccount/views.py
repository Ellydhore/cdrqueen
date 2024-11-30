from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from .forms import ProfileForm, AddressForm
from usermanagement.models import Address

# Profile
@login_required
def profile(request):  
    formatted_phone_number = request.user.phone_number
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form, 'formatted_phone_number': formatted_phone_number})
#
#
# Address
@login_required
def address(request):
    user = request.user
    addresses = Address.objects.filter(user=user)
    
    return render(request, 'address.html', {'addresses': addresses})
#
#
# Add Address
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                address = form.save(commit=False)
                address.user = request.user

                # Check if the new address is set as default
                if address.address_type == 'default':
                    Address.objects.filter(user=request.user, address_type='default').update(address_type='pickup_address')
                
                address.save()

            return redirect('address')
    else:
        form = AddressForm()
    return render(request, 'address.html', {'form': form})
# 
#
# Delete Address
@login_required
def delete_address(request, address_id):
    if request.method == "POST":
        address = get_object_or_404(Address, id=address_id, user=request.user)
        address.delete()
        return redirect('address')
    return redirect('address')
#
#
# Default Address
@login_required
def set_default_address(request, address_id):
    if request.method == "POST":
        address = get_object_or_404(Address, id=address_id, user=request.user)
        Address.objects.filter(user=request.user, address_type='default').update(address_type='pickup_address')

        address.address_type = 'default'
        address.save()

        return redirect('address')
    else:
        return redirect('address')
#
#
# Bank
def bank_and_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'bank_and_cards.html')

