from django.contrib import admin
from .models import About, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('name', 'email')
