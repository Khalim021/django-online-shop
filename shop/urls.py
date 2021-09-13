
from django.urls import path

from shop.views import ShopListView, ProductsDetailView

app_name = 'shop'

urlpatterns = [
    path('', ShopListView.as_view(), name='shop-list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name='detail-view'),
]




