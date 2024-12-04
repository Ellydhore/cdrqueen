from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from usermanagement.models import Order, OrderItem 
from productmanagement.models import Product, ProductImage 

# Create your views here.
@login_required
def all_purchases(request):
    orders = Order.objects.filter(user=request.user).prefetch_related(
        'order_items__product__images'
    )
    return render(request, 'all_purchases.html', {'orders': orders})

@login_required
def cancelled(request):
    orders = Order.objects.filter(
        user=request.user, 
        status='cancelled'
    ).prefetch_related('order_items__product__images')
    
    return render(request, 'cancelled.html', {'orders': orders})


@login_required
def completed(request):
    orders = Order.objects.filter(
        user=request.user, 
        status='completed'
    ).prefetch_related('order_items__product__images')
    
    return render(request, 'completed.html', {'orders': orders})


@login_required
def return_refund(request):
    orders = Order.objects.filter(
        user=request.user, 
        status='return_refund'
    ).prefetch_related('order_items__product__images')
    
    return render(request, 'return.html', {'orders': orders})

@login_required
def to_receive(request):
    orders = Order.objects.filter(
        user=request.user, 
        status='to_receive'
    ).prefetch_related('order_items__product__images')
    
    return render(request, 'to_receive.html', {'orders': orders})
