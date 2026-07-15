from django import forms
from .models import Ad
from apps.products.models import Product


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['name', 'product', 'channel', 'budget']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-select'}),
            'channel': forms.TextInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }
        labels = {
            'name': 'Название кампании',
            'product': 'Услуга',
            'channel': 'Канал продвижения',
            'budget': 'Бюджет (руб)',
        }
