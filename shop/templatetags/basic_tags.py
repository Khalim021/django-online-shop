from django import template

from wishlist.models import UserActivity

register = template.Library()


@register.simple_tag
def get_lang_url(request, lang):
    url = '/' + lang + request.path[3:]
    return url


@register.simple_tag
def get_price_url(request, x):
    price = request.GET.get('price')
    if price:
        return price.split(';')[x]
    return 'null'


# @register.filter
# def in_wishlist(product, request):
#     return request.user in UserActivity.objects.filter()


@register.filter
def class_name(obj):
    name = str(obj.__class__)
    return name.split('\'')[1]
