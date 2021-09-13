# Generated by Django 3.2.5 on 2021-07-28 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('price_info', models.FloatField()),
                ('banner', models.ImageField(blank=True, null=True, upload_to='banner')),
                ('additional_image', models.ImageField(upload_to='additional')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'banner',
                'verbose_name_plural': 'banners',
            },
        ),
    ]
