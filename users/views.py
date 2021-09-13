from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView

from users.forms import UserProfileModelForm
from users.models import UserProfileModel


class UserProfileUpdateView(UpdateView):
    form_class = UserProfileModelForm
    template_name = 'user-profile.html'

    def get_object(self, queryset=None):
        profile, _ = UserProfileModel.objects.get_or_create(user=self.request.user)

        return profile

    def get_success_url(self):
        return reverse('profile:user')










