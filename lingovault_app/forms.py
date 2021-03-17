from django import forms

from .models import Language


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        labels = {'name': ''}
