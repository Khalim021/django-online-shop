# Create your views here.
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentModelForm
from blog.models import BlogModel, CategoryModel, TagModel


class BlogListView(ListView):
    template_name = 'blog-left-sidebar.html'
    paginate_by = 6

    def get_queryset(self):
        qs = BlogModel.objects.order_by('-pk')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        q = self.request.GET.get('q')

        if q:
            qs = qs.filter(title__icontains=q)

        if category:
            qs = qs.filter(category_id=category)

        if tag:
            qs = qs.filter(tags__id=tag)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = CategoryModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['recent_post'] = BlogModel.objects.order_by('?')[:4]

        return context


class BlogDetailView(DetailView):
    model = BlogModel
    template_name = 'blog-details-left-sidebar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = BlogModel.objects.order_by('?')[:4]

        return context


class CommentView(CreateView):
    form_class = CommentModelForm

    def form_valid(self, form):
        form.instance.blog = get_object_or_404(BlogModel, pk=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog-detail', kwargs={'pk': self.kwargs.get('pk')})

