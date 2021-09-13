from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class CheckoutTemplateView(TemplateView):
    template_name = 'checkout.html'


class CartTemplateView(TemplateView):
    template_name = 'shopping-cart.html'



