from django.db import models
from django.utils import timezone

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('CPU', 'Processor'),
        ('GPU', 'Graphics Card'),
        ('RAM', 'Memory'),
        ('HDD', 'Hard Disk Drive'),
        ('SSD', 'Solid State Drive'),
        # Add other categories as needed
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200, blank=True)  # URL for the product image

    def __str__(self):
        return self.name
