from django import forms
from .models import Review

class FormReview(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'stars']
        
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4}),
        }