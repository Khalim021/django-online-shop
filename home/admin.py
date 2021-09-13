from django.contrib import admin

# Register your models here.
from home.models import Banner, AboutModel


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(AboutModel)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'job', 'email']
    list_filter = ['created_at']
    search_fields = ['name', 'job', 'email']
