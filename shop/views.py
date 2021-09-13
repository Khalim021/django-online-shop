from django.db.models import Min, Max
from django.views.generic import ListView, DetailView

from shop.models import Products, Brand, Category, Color


class ShopListView(ListView):
    template_name = 'shop-left-sidebar.html'
    paginate_by = 6

    def get_queryset(self):
        qs = Products.objects.order_by('-pk')
        category = self.request.GET.get('category')
        color = self.request.GET.get('color')
        brand = self.request.GET.get('brand')
        price = self.request.GET.get('price')

        title = self.request.GET.get('title')
        if title:
            qs = qs.filter(title__icontains=title)

        if category:
            qs = qs.filter(category_id=category)

        if color:
            qs = qs.filter(color__id=color)

        if brand:
            qs = qs.filter(brand_id=brand)

        if price:
            price_from, price_to = price.split(';')
            qs = qs.filter(real_price__gte=price_from, real_price__lte=price_to)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brand.objects.all()
        context['categories'] = Category.objects.all()
        context['colors'] = Color.objects.all()[:9]

        min_price, max_price = Products.objects.aggregate(
            Min('real_price'),
            Max('real_price')
        ).values()

        context['min_price'], context['max_price'] = int(min_price), int(max_price)
        return context


class ProductsDetailView(DetailView):
    template_name = 'single-product.html'
    model = Products

    def get_object(self, queryset=None):
        object = super().get_object()
        object.product_views = object.product_views + 1
        object.save()
        return object
