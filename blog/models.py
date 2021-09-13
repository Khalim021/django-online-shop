from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CategoryModel(models.Model):
    title = models.CharField(max_length=255, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class TagModel(models.Model):
    title = models.CharField(max_length=75, verbose_name=_('title'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class BlogModel(models.Model):
    title = models.CharField(max_length=125, verbose_name=_('title'))
    video = models.FileField(upload_to='videos/%y', default=False, verbose_name=_('video'))
    author = models.CharField(max_length=125, verbose_name=_('author'))
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.CASCADE,
                                 related_name='blog', verbose_name=_('category'))
    tags = models.ManyToManyField(TagModel, related_name='blog', verbose_name=_('tags'))
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = RichTextField(verbose_name=_('long_description'))
    extra_content = RichTextField(verbose_name=_('extra content'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))

    def get_comments(self):
        return self.comments.order_by('-date_added')[:3]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog')
        verbose_name_plural = _('blogs')


class CommentModel(models.Model):
    blog = models.ForeignKey(BlogModel,
                             related_name='comments',
                             on_delete=models.CASCADE, verbose_name=_('blog'))
    first_name = models.CharField(max_length=255, verbose_name=_('name'))
    last_name = models.CharField(max_length=255, verbose_name=_('second name'))
    comment = models.TextField(verbose_name=_('comment'))
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=_('date_added'))

    def __str__(self):
        return '%s - %s' % (self.blog.title, self.first_name)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

