from .models import CollaborateRequest
from django import forms


class CollanorateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)