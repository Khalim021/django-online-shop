from django import forms

from blog.models import CommentModel


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        exclude = ['date_added', 'blog']














