from django.shortcuts import render, redirect

# Create your views here.

def view_shopping_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'shopping_bag/shopping_bag.html')

def add_to_shopping_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # get shopping bag or creates one if none existant
    shopping_bag = request.session.get('shopping_bag', {})

    # Add or change quantity of item in shopping bag
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    # updated shopping bag for this session
    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)
    