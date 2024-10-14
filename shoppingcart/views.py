from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_shopping_cart(request):
    return render(request, 'shoppingcart.html')
