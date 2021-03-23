from django import forms

from .models import Language, Post


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']
        labels = {'name': ''}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
