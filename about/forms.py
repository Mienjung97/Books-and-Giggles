from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form for submitting contact requests.
    """

    class Meta:
        model = Contact
        fields = ('name', 'email', 'subject', 'message')
