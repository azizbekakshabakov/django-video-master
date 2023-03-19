from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddVideoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].empty_label = 'User undefined'

    class Meta:
        model = Video
        fields = ['index', 'slug', 'name', 'video', 'preview', 'user_id']
        widgets = {
            'index': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'preview': forms.FileInput(attrs={'class': 'form-control'}),
            'user_id': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Name is longer than 200 symbols')

        return name

class AddCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_id'].empty_label = 'User undefined'
        self.fields['video_id'].empty_label = 'Video undefined'

    class Meta:
        model = Comment
        fields = ['content', 'user_id', 'video_id']
        widgets = {
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'user_id': forms.Select(attrs={'class': 'form-select'}),
            'video_id': forms.Select(attrs={'class': 'form-select'})
        }

    def clean_name(self):
        content = self.cleaned_data['content']
        if len(content) > 3000:
            raise ValidationError('Comment is longer than 3000 symbols')

        return content

