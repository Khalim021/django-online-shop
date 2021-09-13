from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _
from wishlist.models import UserActivity

UserModel = get_user_model()


class Brand(models.Model):
    title = models.CharField(max_length=25, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class Category(models.Model):
    title = models.CharField(max_length=35, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Color(models.Model):
    code = models.CharField(max_length=512, verbose_name=_('code'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    image = models.ImageField(upload_to='product', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(default=0, verbose_name=_('real_price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT,
                              related_name='product', verbose_name=_('brand'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT,
                                 related_name='product', verbose_name=_('category'))
    color = models.ManyToManyField(Color,
                                   related_name='product', verbose_name=_('color'))
    product_views = models.IntegerField(default=0, null=True, blank=True, verbose_name=_('product_views'))

    likes = GenericRelation(UserActivity, related_query_name='likes', verbose_name=_('likes'))

    long_description = RichTextField(verbose_name=_('long_description'))
    additional_definition = models.TextField(verbose_name=_('additional_definition'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def get_related_products(self):
        return self.category.product.exclude(pk=self.pk)

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class ProductImageModel(models.Model):
    product = models.ForeignKey(Products, related_name='images',
                                on_delete=models.CASCADE, verbose_name=_('product'))
    image = models.ImageField(upload_to='product', verbose_name=_('image'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('product image')
        verbose_name_plural = _('product images')
