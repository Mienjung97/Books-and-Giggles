from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Author, Category
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.all()
    query = None
    categories = None
    authors = None
    sort = None
    direction = None


    if request.GET:
        # for making sorting and sorting direction possible
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'author':
                sortkey = 'author__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        # for setting the categories for the nav links: 
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        
        # for setting an author id for the author page: 
        if 'author' in request.GET:
            author_id = request.GET['author']
            products = products.filter(author__id=author_id)
            authors = Author.objects.filter(id=author_id)

        # for processing the search: 
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
            # distinct() removes duplicate search results
            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_authors': authors,
        'current_sorting': current_sorting,
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


def all_authors(request):
    """
    A view to show individual product details
    """

    authors = Author.objects.all()

    context = {
        'authors': authors,
    }

    return render(request, 'authors/authors.html', context)
