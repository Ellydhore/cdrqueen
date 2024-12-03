from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from usermanagement.models import CartItem, ShoppingCart
from productmanagement.models import Product

@login_required
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Use discounted price if applicable
    effective_price = product.discount if product.discount else product.price

    return render(request, 'productdetail.html', {'product': product, 'effective_price': effective_price})


@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)

        # Calculate the effective price
        effective_price = product.discount if product.discount else product.price

        # Get the current user's shopping cart
        cart, created = ShoppingCart.objects.get_or_create(user=request.user)

        # Retrieve the quantity from the POST request
        quantity = request.POST.get('quantity', 1)
        try:
            quantity = int(quantity)
        except ValueError:
            quantity = 1  # Fallback to 1 if conversion fails

        # Calculate the subtotal
        subtotal = effective_price * quantity

        # Check if the item is already in the cart
        existing_item = CartItem.objects.filter(cart=cart, product=product).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.subtotal = existing_item.quantity * effective_price
            existing_item.save()
        else:
            # Create a new CartItem
            CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=quantity,
                subtotal=subtotal
            )

        # Redirect to the shopping cart or product detail page
        return redirect('shopping_cart')
 
