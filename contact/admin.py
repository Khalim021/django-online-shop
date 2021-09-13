from django.contrib import admin

# Register your models here.
from contact.models import ContactModel, FaqModel


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    search_fields = ['full_name', 'email']
    list_filter = ['created']


@admin.register(FaqModel)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']



