
from django import forms

from users.models import UserProfileModel


class UserProfileModelForm(forms.ModelForm):
    class Meta:
        model = UserProfileModel
        exclude = ['user']








