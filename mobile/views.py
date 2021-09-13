# Create your views here.
from django.db.models import Min, Max
from django.views.generic import ListView, DetailView

from mobile.models import MobilePhone, PhoneBrand, PhoneCategory, PhoneColor


class MobileListView(ListView):
    template_name = 'mobile-phones.html'
    paginate_by = 6

    def get_queryset(self):
        q = MobilePhone.objects.order_by('-pk')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        price = self.request.GET.get('price')
        color = self.request.GET.get('color')
        if brand:
            q = q.filter(brand_id=brand)

        if price:
            price_from, price_to = price.split(';')
            q = q.filter(real_price__gte=price_from, real_price__lte=price_to)

        if category:
            q = q.filter(category_id=category)

        if color:
            q = q.filter(color__id=color)

        return q

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = PhoneBrand.objects.all()
        context['categories'] = PhoneCategory.objects.all()
        context['colors'] = PhoneColor.objects.all()

        min_price, max_price = MobilePhone.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()

        context['min_price'], context['max_price'] = int(min_price), int(max_price)

        return context


class MobileDetailView(DetailView):
    template_name = 'mobile-detail-view.html'
    model = MobilePhone

    def get_object(self, queryset=None):
        object = super().get_object()
        object.post_views = object.post_views + 1
        object.save()
        return object
