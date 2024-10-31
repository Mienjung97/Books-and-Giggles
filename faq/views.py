from django.shortcuts import render
from .models import Faq

# Create your views here.


def faq(request):
    """
    A view to render the FAQ page
    """

    faq = Faq.objects.all()
    context = {
        'faq': faq,
    }
    template = 'faq/faq.html'
    return render(request, template, context)
