from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class MobileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mobile'
    verbose_name = _('mobile')

    def ready(self):
        import mobile.signals
