from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from wishlist.models import UserActivity

UserModel = get_user_model()


class PhoneBrand(models.Model):
    title = models.CharField(max_length=122, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('phone brand')
        verbose_name_plural = _('phone brands')


class PhoneCategory(models.Model):
    title = models.CharField(max_length=122, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('phone category')
        verbose_name_plural = _('phone categories')


class PhoneColor(models.Model):
    code = models.CharField(max_length=122, verbose_name=_('code'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('phone color')
        verbose_name_plural = _('phone colors')


class MobilePhone(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='phones', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(default=0, verbose_name=_('real price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    brand = models.ForeignKey(PhoneBrand,
                              on_delete=models.CASCADE,
                              related_name='mobile', verbose_name=_('brand'))
    category = models.ForeignKey(PhoneCategory,
                                 on_delete=models.CASCADE,
                                 related_name='mobile', verbose_name=_('category'))
    color = models.ManyToManyField(PhoneColor, related_name='mobile', verbose_name=_('color'))
    post_views = models.IntegerField(default=0, null=True, blank=True, verbose_name=_('post views'))

    likes = GenericRelation(UserActivity, related_query_name='likes', verbose_name=_('likes'))

    long_description = RichTextField(verbose_name=_('long_description'))
    additional_info = models.TextField(verbose_name=_('additional info'))
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def get_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def get_related_products(self):
        return self.category.mobile.exclude(pk=self.pk)

    class Meta:
        verbose_name = _('mobile phone')
        verbose_name_plural = _('mobile phones')


class PhoneImage(models.Model):
    product = models.ForeignKey(MobilePhone, related_name='mobile',
                                on_delete=models.CASCADE, verbose_name=_('product'))
    image = models.ImageField(upload_to='phone', verbose_name=_('image'))

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = _('mobile image')
        verbose_name_plural = _('mobile images')
