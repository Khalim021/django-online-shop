# Generated by Django 3.2.5 on 2021-08-05 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210805_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogmodel',
            old_name='video_image',
            new_name='video',
        ),
    ]
