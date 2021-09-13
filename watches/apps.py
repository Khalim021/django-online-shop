from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WatchesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'watches'
    verbose_name = _('watches')

    def ready(self):
        import watches.signals


