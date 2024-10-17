from django.contrib import admin
from .models import Product, Category, Author, Cover


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_categories',
        'author',
        'cover',
        'price',
        'image',
        'sku',
    )

    # since one book can have more than one category, this is the helper function:
    # It sorts through the current product, checks for categories and joins them
    # with a comma. The last line just changes the display name in the Admin panel
    def get_categories(self, product):
        return ', '.join(
            [category.name for category in product.category.all()]
        )

    get_categories.short_description = 'Categories'

    ordering = ('author',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class CoverAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Cover, CoverAdmin)
