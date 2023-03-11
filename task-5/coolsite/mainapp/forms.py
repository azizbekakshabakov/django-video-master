from django import forms
from .models import *

class AddVideoForm(forms.Form):
    index = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    preview = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    video = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    user_id = forms.ModelChoiceField(queryset=User.objects.all(), empty_label='User undefined', widget=forms.Select(attrs={'class': 'form-select'})) # required=False, initial=True