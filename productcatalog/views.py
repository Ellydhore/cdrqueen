from django.shortcuts import render
from django.db.models import Q
from productmanagement.models import Product, Category, ProductImage

# Create your views here.
def foo_product_catalog(request):
    # Retrieve query parameters
    query = request.GET.get('query', '')
    category_slug = request.GET.get('category', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    # Retrieve all products, filter by query
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Filter products by category
    category = None
    if category_slug:
        category = Category.objects.filter(slug=category_slug).first()
        if category:
            products = products.filter(category=category)

    # Filter products by price range
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    # Get top 5 most purchased products in the selected category for the carousel
    trending_products = products.order_by('-purchase_count')[:5] if category else []

    context = {
        'products': products,
        'trending_products': trending_products,
        'query': query,
        'category': category,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'prodcatalog.html', context)
