from django.urls import path

from watches.views import WatchListView, WatchesDetailView

app_name = 'watch'

urlpatterns = [
    path('', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>/', WatchesDetailView.as_view(), name='watch-view'),
]



