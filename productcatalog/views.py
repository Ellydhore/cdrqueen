from django.shortcuts import render
from django.db.models import Q
from .models import Product

#import category 

# Create your views here.
def foo_product_catalog(request):
    products = Product.objects.all()
    query = request.GET.get('query', '')
    category = request.GET.get('category', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    print(f"Query: {query}, Category: {category}, Min Price: {min_price}, Max Price: {max_price}")


    # Search functionality
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    if category:
        products = products.filter(category=category)

    # Filter by price range
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'products': products,
        'query': query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'prodcatalog.html', context)
