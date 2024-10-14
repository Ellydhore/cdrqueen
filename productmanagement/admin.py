from django.contrib import admin
from .models import Category, Subcategory, Brand, Product, ProductImage, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Review)
