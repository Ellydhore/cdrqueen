from decimal import Decimal
from django.shortcuts import render, redirect
from usermanagement.models import ShoppingCart, Address, Card, CartItem


def get_cart_summary(request):
    """
    Retrieves the shopping cart details and computes totals for the logged-in user.
    """
    try:
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = cart.items.all()

        cart_items_data = []
        for item in cart_items:
            item_total = Decimal(item.product.price) * Decimal(item.quantity)
            cart_items_data.append({
                'item': item,
                'item_total': item_total,
            })

        subtotal = sum(data['item_total'] for data in cart_items_data)
        store_pickup = Decimal("99.00")
        tax = subtotal * Decimal("0.025")
        total_price = subtotal + store_pickup + tax
    except ShoppingCart.DoesNotExist:
        cart_items_data = []
        subtotal = store_pickup = tax = total_price = Decimal("0.00")

    return {
        'cart_items_data': cart_items_data,
        'subtotal': subtotal,
        'store_pickup': store_pickup,
        'tax': tax,
        'total_price': total_price,
    }

def get_user_addresses(request):
    """
    Retrieves the default address and all addresses for the logged-in user.
    """
    try:
        default_address = Address.objects.get(user=request.user, address_type='default')
    except Address.DoesNotExist:
        default_address = None

    all_addresses = Address.objects.filter(user=request.user)

    return {
        'default_address': default_address,
        'all_addresses': all_addresses,
    }

def get_user_cards(request):
    """
    Retrieves all card details for the logged-in user.
    """
    cards = Card.objects.filter(user=request.user)
    return {
        'cards': cards,
    }

def checkout_view(request):
    """
    Combines cart summary, address details, and payment card details to display the checkout page.
    """
    if not request.user.is_authenticated:
        return redirect('login')

    # Retrieve cart summary, user addresses, and cards
    cart_summary = get_cart_summary(request)
    user_addresses = get_user_addresses(request)
    user_cards = get_user_cards(request)

    # Combine context data
    context = {
        **cart_summary,
        **user_addresses,
        **user_cards,
    }

    return render(request, 'checkout.html', context)

def payment_view(request):
    """
    Combines cart summary, address details, and payment card details to display the checkout page.
    """
    if not request.user.is_authenticated:
        return redirect('login')

    # Retrieve cart summary, user addresses, and cards
    cart_summary = get_cart_summary(request)
    user_addresses = get_user_addresses(request)
    user_cards = get_user_cards(request)

    # Combine context data
    context = {
        **cart_summary,  # Includes cart_items_data, subtotal, tax, etc.
        **user_addresses,
        **user_cards,
    }

    return render(request, 'payment.html', context)

