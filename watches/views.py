from django.db.models import Min, Max
from django.views.generic import ListView, DetailView

from watches.models import WatchBrand, WatchCategory, WatchColor, WatchModel


class WatchListView(ListView):
    template_name = 'smartwatch_list.html'
    paginate_by = 6

    def get_queryset(self):
        qsl = WatchModel.objects.order_by('-pk')
        brand = self.request.GET.get('brand')
        cate = self.request.GET.get('category')
        cor = self.request.GET.get('color')
        price = self.request.GET.get('price')

        if price:
            price_from, price_to = price.split(';')
            qsl = qsl.filter(real_price__gte=price_from, real_price__lte=price_to)

        if cor:
            qsl = qsl.filter(color__id=cor)

        if cate:
            qsl = qsl.filter(category_id=cate)

        if brand:
            qsl = qsl.filter(brand_id=brand)

        return qsl

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = WatchBrand.objects.all()
        context['categories'] = WatchCategory.objects.all()
        context['colors'] = WatchColor.objects.all()

        min_price, max_price = WatchModel.objects.aggregate(
            Min('real_price'),
            Max('real_price'),
        ).values()

        context['min_price'], context['max_price'] = int(min_price), int(max_price)
        return context


class WatchesDetailView(DetailView):
    template_name = 'watch-detail.html'
    model = WatchModel

    def get_object(self, queryset=None):
        object = super().get_object()
        object.post_views = object.post_views + 1
        object.save()
        return object
