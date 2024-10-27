from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Author, Category
from .forms import ProductForm, AuthorForm, CategoryForm

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


@login_required
def add_product(request):
    """
    Add a product to the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


# need to create templates, urls and finish the view:

@login_required
def add_author(request):
    """
    Add a new author while on frontend
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added author!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add author. Please ensure the form is valid.')
    else:
        form = AuthorForm()

    template = 'authors/add_author.html'
    context = {
        'form': form,
    }

    return render(request, template, context)




@login_required
def add_category(request):
    """
    Add a new caategory while on frontend
    """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added category!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Failed to add category. Please ensure the form is valid.')
    else:
        form = CategoryForm()

    template = 'categories/add_category.html'
    context = {
        'form': form,
    }

    return render(request, template, context)