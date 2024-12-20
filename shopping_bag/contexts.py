from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    shopping_bag = request.session.get('shopping_bag', {})

    # Check if the shopping bag is empty to not
    # show delivery cost on empty basket
    if not shopping_bag:
        context = {
            'shopping_bag_items': [],
            'total': Decimal('0'),
            'product_count': 0,
            'delivery': Decimal('0'),
            'free_delivery_delta': settings.FREE_DELIVERY_THRESHOLD,
            'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
            'grand_total': Decimal('0'),
        }
        return context

    # function to display items in shopping bag for all pages
    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shopping_bag_items.append(
            {
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            }
        )

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_COST
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0')
        free_delivery_delta = Decimal('0')

    grand_total = delivery + total

    context = {
        'shopping_bag_items': shopping_bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
