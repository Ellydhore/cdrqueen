from django.shortcuts import render, redirect

# Create your views here.
def all_purchases(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'all_purchases.html')

def cancelled(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'cancelled.html')

def completed(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'completed.html')

def return_refund(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'return.html')

def to_receive(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'to_receive.html')
