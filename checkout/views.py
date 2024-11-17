from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_checkout(request):
    return render(request, 'checkout.html')