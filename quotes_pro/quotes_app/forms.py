from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = '__all__'

        widgets = {
            'id': forms.NumberInput(attrs={'class': 'form-control'}),
            'quotes': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'})
        }