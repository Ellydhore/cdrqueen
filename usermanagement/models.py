from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.conf import settings
from productmanagement.models import Product

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    gender = models.CharField(default='O', max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    date_of_birth = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.email

class ShoppingCart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)


class Address(models.Model):
    ADDRESS_LABEL_CHOICES = [
        ('home', 'Home'),
        ('work', 'Work')
    ]

    ADDRESS_TYPE_CHOICES = [
        ('default', 'Default'),
        ('pickup_address', 'Pickup Address'),
        ('return_address', 'Return Address')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255, blank=True)
    barangay = models.CharField(max_length=255, blank=True) 
    city = models.CharField(max_length=255, blank=True)
    province = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    specific_location = models.CharField(max_length=255, blank=True)
    address_label = models.CharField(max_length=10, choices=ADDRESS_LABEL_CHOICES, default='Home')
    address_type = models.CharField(max_length=15, choices=ADDRESS_TYPE_CHOICES, default='Default')

    def __str__(self):
        return f"{self.get_address_label_display()} - {self.street}, {self.city}"

class Bank(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='bank_detail')
    bank_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=50, unique=True)

class Card(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cards')
    card_number = models.CharField(max_length=16, unique=True)
    expiry_date = models.DateField()
    cardholder_name = models.CharField(max_length=255)

class Order(models.Model):
    STATUS_CHOICES = [
        ('to_receive', 'To Receive'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('return_refund', 'Return/Refund')
    ]
    DELIVERY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('returned', 'Returned')
    ]
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    delivery_status = models.CharField(max_length=20, choices=DELIVERY_STATUS_CHOICES, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date_delivered = models.DateField(null=True, blank=True)
    date_returned = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Order {self.id} - {self.user.username} - {self.get_delivery_status_display()}"


class DeliveryStatusUpdate(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='delivery_status_updates')
    status = models.CharField(max_length=20, choices=Order.DELIVERY_STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']  # Ensures the updates are ordered by time

    def __str__(self):
        return f"{self.get_status_display()} at {self.timestamp} for Order {self.order.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity} for Order {self.order.id}"
