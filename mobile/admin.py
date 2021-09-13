from django.contrib import admin

# Register your models here.
from mobile.forms import ColorModelForm
from mobile.models import PhoneBrand, PhoneCategory, PhoneColor, MobilePhone, PhoneImage


@admin.register(PhoneBrand)
class PhoneBrandAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(PhoneCategory)
class PhoneCategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(PhoneColor)
class PhoneColorAdmin(admin.ModelAdmin):
    list_display = ['code']
    search_fields = ['code']
    form = ColorModelForm


class PhoneImageStackedInline(admin.StackedInline):
    model = PhoneImage


@admin.register(MobilePhone)
class MobilePhoneAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'brand', 'category', 'discount']
    search_fields = ['title', 'brand', 'category', 'long_description']
    list_filter = ['brand', 'category']
    autocomplete_fields = ['category', 'brand', 'color']
    readonly_fields = ['real_price']
    inlines = [PhoneImageStackedInline]
