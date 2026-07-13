from django import forms
from .models import Contract
from apps.products.models import Product


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "name",
            "product",
            "file",
            "start_date",
            "end_date",
            "cost",
            "customer"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "product": forms.Select(attrs={"class": "form-select"}),
            "file": forms.FileInput(attrs={"class": "form-control"}),
            "start_date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "end_date": forms.NumberInput(attrs={"type": "date", "class": "form-control"}),
            "cost": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "customer": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "name": "Название контракта",
            "product": "Услуга",
            "file": "Файл контракта",
            "start_date": "Дата заключения",
            "end_date": "Дата истечения",
            "cost": "Сумма",
            "customer": "Клиент",
        }
