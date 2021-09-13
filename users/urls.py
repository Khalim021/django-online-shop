from django.urls import path

from users.views import UserProfileUpdateView

app_name = 'profile'

urlpatterns = [
    path('', UserProfileUpdateView.as_view(), name='user')
]








