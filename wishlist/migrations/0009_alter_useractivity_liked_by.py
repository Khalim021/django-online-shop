# Generated by Django 3.2.5 on 2021-09-06 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0008_auto_20210906_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='liked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='liked_by'),
        ),
    ]
