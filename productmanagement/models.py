from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError

# CATEGORY
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# SUBCATEGORY
class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} - {self.name}"

# BRAND
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# PRODUCT
class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Allow no discount
    stock = models.PositiveIntegerField(blank=False, null=False)
    manufacturer = models.CharField(max_length=255, blank=False, null=False)
    num_of_purchases = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=255, blank=True, null=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    num_of_ratings = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Please provide a rating between 1 and 5."
    ) 

    ave_ratings = models.DecimalField(max_digits=3, decimal_places=2, 
        default=0.00, validators=[MinValueValidator(1), 
        MaxValueValidator(5)], 
        help_text="Please provide a rating between 1 and 5.")

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')

    keywords = models.CharField(max_length=255, blank=False, null=False, help_text="Enter at least 4 keywords, separated by commas")

    # Monitor-specific fields
    screen_size = models.CharField(max_length=50, blank=True, null=True)
    resolution = models.CharField(max_length=50, blank=True, null=True)
    aspect_ratio = models.CharField(max_length=20, blank=True, null=True)

    def clean(self):
        # Ensure at least 4 keywords are provided
        keywords_list = self.keywords.split(',')
        if len(keywords_list) < 4:
            raise ValidationError("A product must have at least 4 keywords.")

    def __str__(self):
        return self.name

# PRODUCT IMAGE
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image_url_1 = models.URLField(max_length=200, default="https://media.istockphoto.com/id/1147544807/vector/thumbnail-image-vector-graphic.jpg?s=612x612&w=0&k=20&c=rnCKVbdxqkjlcs3xH87-9gocETqpspHFXu5dIGB4wuM=")
    image_url_2 = models.URLField(max_length=200, null=True, blank=True)
    image_url_3 = models.URLField(max_length=200, null=True, blank=True)
    image_url_4 = models.URLField(max_length=200, null=True, blank=True)
    image_url_5 = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.product.name} Image"

# USER REVIEW
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('product', 'user')  # Prevent a user from reviewing the same product multiple times

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username} - {self.rating}/5"
