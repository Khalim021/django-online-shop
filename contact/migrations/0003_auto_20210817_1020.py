# Generated by Django 3.2.5 on 2021-08-17 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20210817_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faqmodel',
            name='content',
        ),
        migrations.RemoveField(
            model_name='faqmodel',
            name='extra_title',
        ),
    ]
