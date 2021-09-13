from django import forms

from shop.models import Color


class ShopColorModelForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'code': forms.TextInput(attrs={
                'type': 'color'
            })
        }






