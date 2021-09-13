from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ContactModel(models.Model):
    full_name = models.CharField(max_length=255, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    subject = models.CharField(max_length=255, verbose_name=_('subject'))
    message = models.TextField(verbose_name=_('message'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class FaqModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('faq')
        verbose_name_plural = _('faqs')
