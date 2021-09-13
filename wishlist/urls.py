from django.urls import path

from wishlist.views import WishListView, add_wishlist

app_name = 'wishlist'

urlpatterns = [
    path('', WishListView.as_view(), name='user-wishlist'),
    path('wishlist/<int:pk>/<str:klass>/', add_wishlist, name='add-wishlist'),
]
