from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CheckoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkouts'
    verbose_name = _('checkouts')
