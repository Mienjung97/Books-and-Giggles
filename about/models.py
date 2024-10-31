from django.db import models
from django import forms

# Create your models here.

class About(models.Model):
    """
    Stores a single about me text.
    """

    title = models.CharField(max_length=200, unique=True)
    about_image = models.ImageField(null=True, blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    """
    Gives the user the ability to contact the page admin
    """
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=254, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=2000, blank=False)

    def __str__(self):
        return f"Contact request from {self.name}" # This string might get changed down the road

