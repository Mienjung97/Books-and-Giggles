from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields = '__all__'