# Generated by Django 3.2.5 on 2021-09-01 08:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wishlist', '0003_alter_useractivity_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractivity',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
