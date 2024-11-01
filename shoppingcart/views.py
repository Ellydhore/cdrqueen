from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from usermanagement.models import ShoppingCart, CartItem

@login_required
def shopping_cart(request):
    # Get the ShoppingCart for the logged-in user
    cart = ShoppingCart.objects.filter(user=request.user).first()

    # If the user has a cart, fetch all related CartItems
    cart_items = []
    if cart:
        cart_items = CartItem.objects.filter(cart=cart)

    # Calculate the total price of the cart items
    total_price = sum(item.subtotal for item in cart_items)

    # Render the shopping cart template with cart items and total price
    return render(request, 'shoppingcart.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })
