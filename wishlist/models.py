from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class UserActivity(models.Model):
    liked_by = models.ForeignKey(UserModel, null=True, blank=True,
                                 related_name='likes',
                                 on_delete=models.CASCADE,
                                 verbose_name=_('liked_by'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))
    content_type = models.ForeignKey(ContentType,
                                     on_delete=models.CASCADE,
                                     related_name='likes')
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')












