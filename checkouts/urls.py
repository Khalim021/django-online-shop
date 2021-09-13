from django.urls import path

from checkouts.views import CheckoutTemplateView, CartTemplateView

app_name = 'checkouts'

urlpatterns = [
    path('', CheckoutTemplateView.as_view(), name='checkouts'),
    path('cart/', CartTemplateView.as_view(), name='cart'),
]








