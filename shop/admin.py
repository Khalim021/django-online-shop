from django.contrib import admin

from shop.forms import ShopColorModelForm
from shop.models import Brand, Category, Color, ProductImageModel, Products, UserActivity


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created']


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_filter = ['created']
    search_fields = ['code']
    form = ShopColorModelForm


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImageModel


admin.site.register(UserActivity)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'brand', 'category', 'discount']
    search_fields = ['title', 'brand', 'category', 'long_description']
    list_filter = ['created', 'brand', 'category']
    autocomplete_fields = ['category', 'brand', 'color']
    readonly_fields = ['real_price']
    inlines = [ProductImageStackedInline]
