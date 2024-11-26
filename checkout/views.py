from decimal import Decimal
from django.shortcuts import render, redirect
from usermanagement.models import ShoppingCart, CartItem

def checkout_view(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect unauthenticated users

    try:
        # Retrieve the shopping cart for the logged-in user
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = cart.items.all()

        # Precompute item total prices
        cart_items_data = []
        for item in cart_items:
            item_total = Decimal(item.product.price) * Decimal(item.quantity)
            cart_items_data.append({
                'item': item,
                'item_total': item_total,
            })

        # Calculate subtotal by summing item_total for all items
        subtotal = sum(data['item_total'] for data in cart_items_data)
        store_pickup = Decimal("99.00")  # Fixed store pickup fee
        tax = subtotal * Decimal("0.025")  # Example: 2.5% tax rate
        total_price = subtotal + store_pickup + tax  # Final total
    except ShoppingCart.DoesNotExist:
        # If no cart exists for the user
        cart_items_data = []
        subtotal = store_pickup = tax = total_price = Decimal("0.00")

    context = {
        'cart_items_data': cart_items_data,
        'subtotal': subtotal,
        'store_pickup': store_pickup,
        'tax': tax,
        'total_price': total_price,
    }
    return render(request, 'checkout.html', context)
