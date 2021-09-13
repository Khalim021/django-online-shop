from django.urls import path

from mobile.views import MobileListView, MobileDetailView

app_name = 'mobile'

urlpatterns = [
    path('', MobileListView.as_view(), name='mobile-list'),
    path('<int:pk>/', MobileDetailView.as_view(), name='mobile-view'),
]
