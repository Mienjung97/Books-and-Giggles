from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names_c = [(c.id, c.get_friendly_name()) for c in categories]
        authors = author.objects.all()
        friendly_names_a = [(a.id, a.get_friendly_name()) for a in authors]


        self.fields['category'].choices = friendly_names_c
        self.fields['author'].choices = friendly_names_a
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'