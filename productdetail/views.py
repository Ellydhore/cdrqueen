from django.shortcuts import render, HttpResponse

# Create your views here.
def foo_product_detail(request):
    return render(request, 'productdetail.html')
