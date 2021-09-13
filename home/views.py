# Create your views here.
from django.views.generic import TemplateView

from blog.models import BlogModel
from home.models import AboutModel
from mobile.models import MobilePhone
from shop.models import Products
from watches.models import WatchModel


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shop'] = Products.objects.order_by('-pk')
        context['watch'] = WatchModel.objects.order_by('-pk')
        context['mobile'] = MobilePhone.objects.order_by('-pk')
        context['blog'] = BlogModel.objects.order_by('-pk')[:4]
        context['teams'] = AboutModel.objects.order_by('-pk')

        return context


class AboutTemplateView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = AboutModel.objects.order_by('-pk')

        return context

