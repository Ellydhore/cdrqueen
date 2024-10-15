from django.shortcuts import render, HttpResponse
from productmanagement.models import Product, ProductImage

# Create your views here.
    
def foo_home(request):
    # Get the top 3 products with the most ratings
    top_rated_products = Product.objects.order_by('-num_of_ratings')[:3]
    most_purchases = Product.objects.order_by('-num_of_purchases')[:6]

    context = {
        'top_rated_products': top_rated_products,
        'most_purchases': most_purchases,
    }

    return render(request, 'home.html', context)

    
    
    
    

    
    
    
    

    
