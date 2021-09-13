from django.contrib import admin

# Register your models here.
from watches.forms import WatchColorModelForm
from watches.models import WatchCategory, WatchColor, WatchModel, WatchBrand, WatchImageModel


@admin.register(WatchColor)
class WatchColorAdmin(admin.ModelAdmin):
    list_display = ['code']
    search_fields = ['code']
    list_filter = ['created']
    form = WatchColorModelForm


@admin.register(WatchCategory)
class WatchCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created']
    search_fields = ['title']


@admin.register(WatchBrand)
class WatchBrandAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created']


class WatchModelStackedInline(admin.StackedInline):
    model = WatchImageModel


@admin.register(WatchModel)
class WatchModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'brand', 'category', 'discount']
    search_fields = ['title', 'brand', 'category', 'long_description']
    list_filter = ['created', 'brand', 'category']
    autocomplete_fields = ['category', 'color', 'brand']
    readonly_fields = ['real_price']
    inlines = [WatchModelStackedInline]
