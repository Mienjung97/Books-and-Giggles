from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Author, Category

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(description2__icontains=query)
                | Q(extra_info__icontains=query)
                | Q(publisher__icontains=query)
                | Q(isbn__icontains=query)
                | Q(author__name__icontains=query)
                | Q(author__friendly_name__icontains=query)
                | Q(category__name__icontains=query)
                | Q(category__friendly_name__icontains=query)
            )
            products = products.filter(queries).distinct()

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
