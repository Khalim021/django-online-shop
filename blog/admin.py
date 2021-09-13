from django.contrib import admin

# Register your models here.
from blog.models import CategoryModel, TagModel, BlogModel, CommentModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['created']


@admin.register(BlogModel)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category']
    search_fields = ['title', 'author', 'category']
    list_filter = ['created']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_filter = ['date_added']
