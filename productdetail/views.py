from django.shortcuts import render, HttpResponse
from productmanagement.models import Product, ProductImage

# Create your views here.
def foo_product_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    context = {
        'product': product
    }
    return render(request, 'productdetail.html', context)
