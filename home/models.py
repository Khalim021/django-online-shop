
from django.db import models
from django.utils.translation import  gettext_lazy as _
from shop.models import Products


class Banner(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    info = models.TextField(verbose_name=_('info'))
    price_info = models.FloatField(verbose_name=_('price info'))
    banner = models.ImageField(upload_to='banner', null=True, blank=True, verbose_name=_('banner'))
    additional_image = models.ImageField(upload_to='additional', verbose_name=_('additional image'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('banner')
        verbose_name_plural = _('banners')


class AboutModel(models.Model):
    name = models.CharField(max_length=125, verbose_name=_('name'))
    image = models.ImageField(upload_to='teammates', verbose_name=_('image'))
    job = models.CharField(max_length=120, verbose_name=_('job'))
    email = models.EmailField(verbose_name=_('email'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('about')
        verbose_name_plural = _('about us')













