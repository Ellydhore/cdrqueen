from django.shortcuts import render
from productmanagement.models import Product, Category, Brand
from django.db.models import Q

def foo_product_catalog(request, category_slug=None):
    # Retrieve query parameters
    query = request.GET.get('query', '')
    category_slug = request.GET.get('category', '')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    selected_brands = request.GET.getlist('brand')

    # Retrieve all products, filtered by query if provided
    products = Product.objects.all()
    if query:
        products = products.filter(Q(name__icontains=query) | Q(description__icontains=query))

    # Filter by category if a slug is provided
    category = None
    if category_slug:
        category = Category.objects.filter(slug=category_slug).first()
        if category:
            products = products.filter(category=category)
    
    # Filter by brands
    if selected_brands:
        products = products.filter(brand__name__in=selected_brands)

    # Filter by price range if provided
    if min_price and max_price:
        products = products.filter(price__gte=min_price, price__lte=max_price)

    # Get top 5 products by average ratings for trending section
    trending_products = Product.objects.order_by('-ave_ratings')[:4]

    # Get all categories and brands for the dropdown
    categories = Category.objects.all()
    brands = Brand.objects.all().order_by('name')

    context = {
        'products': products,
        'trending_products': trending_products,
        'categories': categories,
        'brands': brands,
        'query': query,
        'category': category,
        'selected_brands': selected_brands,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'prodcatalog.html', context)
