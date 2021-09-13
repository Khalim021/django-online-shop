from django.contrib.auth import get_user_model
from django.db import models

from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class UserProfileModel(models.Model):
    profile_pc = models.ImageField(upload_to='profile_pics', null=True, blank=True,
                                   default='images/profile_pics/no_picture.png', verbose_name=_('Profile picture'))
    user = models.OneToOneField(UserModel, null=True, blank=True,
                                on_delete=models.CASCADE,
                                related_name='profile',
                                verbose_name=_('user'))
    first_name = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('name'))
    last_name = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('Second name'))
    phone = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('phone'))
    email = models.EmailField(null=True, blank=True, verbose_name=_('email'))
    country = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('country'))
    address = models.CharField(max_length=50, null=True, blank=True, verbose_name=_('address'))
    city = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('city'))
    state = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('state'))
    postcode = models.CharField(max_length=30, null=True, blank=True, verbose_name=_('postcode'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
