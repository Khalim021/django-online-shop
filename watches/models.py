from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from django.utils.translation import gettext_lazy as _

from wishlist.models import UserActivity

UserModel = get_user_model()


class WatchBrand(models.Model):
    title = models.CharField(max_length=25, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('watch brand')
        verbose_name_plural = _('watch brands')


class WatchCategory(models.Model):
    title = models.CharField(max_length=25, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('watch category')
        verbose_name_plural = _('watch categories')


class WatchColor(models.Model):
    code = models.CharField(max_length=25, verbose_name=_('code'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = _('watch color')
        verbose_name_plural = _('watch colors')


class WatchModel(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    image = models.ImageField(upload_to='watch', verbose_name=_('image'))
    price = models.FloatField(verbose_name=_('price'))
    real_price = models.FloatField(default=0, verbose_name=_('real price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('discount'))
    brand = models.ForeignKey(WatchBrand,
                              on_delete=models.PROTECT,
                              related_name='watches', verbose_name=_('brand'))
    category = models.ForeignKey(WatchCategory,
                                 on_delete=models.PROTECT,
                                 related_name='watches', verbose_name=_('category'))
    color = models.ManyToManyField(WatchColor, related_name='watches', verbose_name=_('color'))
    post_views = models.IntegerField(default=0, null=True, blank=True, verbose_name=_('post views'))

    likes = GenericRelation(UserActivity, related_query_name='likes', verbose_name=_('likes'))

    long_description = RichTextField(verbose_name=_('long_description'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    def is_discount(self):
        return self.discount != 0

    def take_price(self):
        if self.is_discount():
            return self.price - self.price * self.discount / 100
        return self.price

    def get_related_products(self):
        data = WatchModel.objects.filter(category_id=self.category_id).exclude(pk=self.pk)
        return data

    class Meta:
        verbose_name = _('watch')
        verbose_name_plural = _('watches')


class WatchImageModel(models.Model):
    watch = models.ForeignKey(WatchModel, related_name='images',
                              on_delete=models.CASCADE, null=True, blank=True, verbose_name=_('watch'))
    image = models.ImageField(upload_to='watches', null=True, blank=True, verbose_name=_('image'))

    def __str__(self):
        return self.watch.title

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
