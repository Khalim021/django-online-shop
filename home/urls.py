from django.urls import path

from home.views import HomeTemplateView, AboutTemplateView

app_name = 'home'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('about/', AboutTemplateView.as_view(), name='about'),
]












