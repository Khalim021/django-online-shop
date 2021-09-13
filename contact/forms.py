
from django import forms

from contact.models import ContactModel


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['created']










