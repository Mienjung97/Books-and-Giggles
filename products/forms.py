from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Author


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names_c = [(c.id, c.get_friendly_name()) for c in categories]
        authors = Author.objects.all()
        friendly_names_a = [(a.id, a.get_friendly_name()) for a in authors]

        self.fields['category'].choices = friendly_names_c
        self.fields['author'].choices = friendly_names_a
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'
