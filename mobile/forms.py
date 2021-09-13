from django import forms

from mobile.models import PhoneColor


class ColorModelForm(forms.ModelForm):
    class Meta:
        model = PhoneColor
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }





