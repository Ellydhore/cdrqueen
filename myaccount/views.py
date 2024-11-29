from django.shortcuts import render, redirect, get_object_or_404
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
@login_required
def add_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
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
        return redirect('address')  # Redirect back to the address list or a different page
    return redirect('address')  # Fallback to address page if method is not POST
# Bank
def bank_and_cards(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'bank_and_cards.html')

