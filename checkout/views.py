from decimal import Decimal
from django.shortcuts import render, redirect
from usermanagement.models import ShoppingCart, Address, Card, CartItem, Order


def get_cart_summary(request):
    """
    Retrieves the shopping cart details and computes totals for the logged-in user,
    using discounted prices if applicable.
    """
    try:
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = cart.items.all()

        cart_items_data = []
        for item in cart_items:
            # Use discounted price if applicable
            effective_price = item.product.discount if item.product.discount else item.product.price
            item_total = Decimal(effective_price) * Decimal(item.quantity)
            
            cart_items_data.append({
                'item': item,
                'effective_price': effective_price,
                'item_total': item_total,
            })

        # Calculate totals
        subtotal = sum(data['item_total'] for data in cart_items_data)
        store_pickup = Decimal("99.00")
        tax = subtotal * Decimal("0.025")
        total_price = subtotal + store_pickup + tax
    except ShoppingCart.DoesNotExist:
        # Defaults if the cart does not exist
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

def confirm_order_view(request):
    """
    Transfers cart items to an Order and clears the cart.
    """
    try:
        # Get the user's shopping cart
        cart = ShoppingCart.objects.get(user=request.user)
        cart_items = cart.items.all()
        
        if not cart_items.exists():
            # If no items in the cart, redirect to the cart page
            return redirect('shopping_cart')  # Replace 'cart' with the name of your cart URL
        
        # Calculate total amount
        total_amount = sum(
            Decimal(item.product.discount if item.product.discount else item.product.price) * Decimal(item.quantity)
            for item in cart_items
        )
        
        # Create an Order
        order = Order.objects.create(
            user=request.user,
            status='to_receive',
            delivery_status='pending',
            total_amount=total_amount,
            is_paid=False,  # Update this if payment integration is included
        )
        
        # Optional: Associate cart items with the order if using a separate order item model
        
        # Clear the cart
        cart.items.all().delete()
        
        # Redirect to the "to_receive" page
        return redirect('to_receive')  # Replace 'to_receive' with the appropriate URL name
    
    except ShoppingCart.DoesNotExist:
        # Redirect to cart page if the cart doesn't exist
        return redirect('shopping_cart')  # Replace 'cart' with the cart URL name

