from django.db import models


# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Author(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Cover(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField('Category', related_name='products')
    author = models.ForeignKey(
        'Author', null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    description2 = models.TextField(null=True, blank=True)
    extra_info = models.TextField(null=True, blank=True)
    year_published = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)
    cover = models.ForeignKey(
        'Cover', null=True, blank=True, on_delete=models.SET_NULL
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    isbn = models.CharField(max_length=13, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
