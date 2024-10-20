from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

# Create your views here.

def view_shopping_bag(request):
    """
    A view that renders the bag contents page
    """

    return render(request, 'shopping_bag/shopping_bag.html')

def add_to_shopping_bag(request, item_id):
    """
    Add a quantity of the specified product to the shopping bag
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get shopping bag or creates one if none existant
    shopping_bag = request.session.get('shopping_bag', {})

    # Add or change quantity of item on product detail page
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    # updated shopping bag for this session
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)

def adjust_shopping_bag(request, item_id):
    """
    Adjust the quantity of the specified product in the shopping bag
    """

    quantity = int(request.POST.get('quantity'))

    shopping_bag = request.session.get('shopping_bag', {})

    # Change quantity of item in shopping bag
    if quantity >= 0:
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)

    # updated shopping bag for this session
    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag'))

def remove_from_shopping_bag(request, item_id):
    """
    Remove item from shopping bag
    """
    try:
        shopping_bag = request.session.get('shopping_bag', {})

        # remove item from shopping bag
        shopping_bag.pop(item_id, None)

        # updated shopping bag for this session
        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)