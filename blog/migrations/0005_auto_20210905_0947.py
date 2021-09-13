# Generated by Django 3.2.5 on 2021-09-05 04:47

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_commentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='author',
            field=models.CharField(max_length=125, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog', to='blog.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='extra_content',
            field=ckeditor.fields.RichTextField(verbose_name='extra content'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='long_description',
            field=ckeditor.fields.RichTextField(verbose_name='long_description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='short_description',
            field=models.TextField(verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='tags',
            field=models.ManyToManyField(related_name='blog', to='blog.TagModel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='title',
            field=models.CharField(max_length=125, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='video',
            field=models.FileField(default=False, upload_to='videos/%y', verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogmodel', verbose_name='blog'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date_added'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='second name'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='tagmodel',
            name='title',
            field=models.CharField(max_length=75, verbose_name='title'),
        ),
    ]
