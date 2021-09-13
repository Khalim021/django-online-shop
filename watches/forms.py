from django import forms

from watches.models import WatchColor


class WatchColorModelForm(forms.ModelForm):
    class Meta:
        model = WatchColor
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }





