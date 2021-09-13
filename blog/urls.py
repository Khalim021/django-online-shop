from django.urls import path

from blog.views import BlogListView, BlogDetailView, CommentView

app_name = 'blog'

urlpatterns = [

    path('<int:pk>/comment-create/', CommentView.as_view(), name='comment-create'),
    path('', BlogListView.as_view(), name='blog-list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

]
