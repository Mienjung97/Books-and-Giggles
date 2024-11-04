from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import About, Contact
from .forms import ContactForm

# Create your views here.


def about(request):
    """
    Renders the About page and contact form
    """
    about = About.objects.all().order_by('-updated_on').first()

    template = 'about/about.html'
    context = {
        'about': about,
    }

    return render(request, template, context)


def contact(request):
    """
    Renders the contact us form on seperate page
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            print(form)
            messages.success(
                request,
                "Your message has been received! We will respond to your message within 3 business days.",
            )

            return redirect(reverse('home'))
        else:
            messages.error(
                request,
                'Failed to send a message. Please ensure the form is valid.',
            )
    else:
        form = ContactForm()

    template = 'about/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def newsletter(request):
    """
    A view to return the newsletter page
    """

    return render(request, 'about/newsletter.html')
