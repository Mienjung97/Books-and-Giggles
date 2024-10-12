from django.contrib import admin
from. models import Product, Category, Author, Cover

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Cover)