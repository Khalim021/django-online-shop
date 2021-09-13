from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from mobile.models import MobilePhone
from shop.models import Products
from watches.models import WatchModel

UserModel = get_user_model()


class CheckoutsModel(models.Model):
    user = models.ForeignKey(UserModel, related_name='orders', on_delete=models.CASCADE, verbose_name=_('user'))
    products = models.ManyToManyField(Products, related_name='checkouts', verbose_name=_('products'))
    watches = models.ManyToManyField(WatchModel, related_name='checkouts', verbose_name=_('watches'))
    mobile = models.ManyToManyField(MobilePhone, related_name='checkouts', verbose_name=_('mobile phones'))
    price = models.FloatField(null=True, verbose_name=_('price'))
    first_name = models.CharField(max_length=30, verbose_name=_('name'))
    last_name = models.CharField(max_length=30, verbose_name=_('second name'))
    phone = models.CharField(max_length=30, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    country = models.CharField(max_length=30, verbose_name=_('country'))
    company = models.CharField(max_length=75, verbose_name=_('company'))
    address1 = models.CharField(max_length=50, verbose_name=_('address'))
    city = models.CharField(max_length=30, verbose_name=_('city'))
    state = models.CharField(max_length=30, verbose_name=_('state'))
    postcode = models.CharField(max_length=30, verbose_name=_('postcode'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return str(f'{self.user} + {self.last_name}')

    class Meta:
        verbose_name = _('checkout')
        verbose_name_plural = _('checkouts')





















