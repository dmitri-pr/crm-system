from django import forms
from .models import Contract
from apps.services.models import Service


class ContractCreateForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            "name",
            "service",
            "file",
            "date_signed",
            "validity_period",
            "amount",
            "active_client"
        ]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "service": forms.Select(attrs={"class": "form-select"}),
            "file": forms.FileInput(attrs={"class": "form-control"}),
            "date_signed": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "validity_period": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Например: 365"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "active_client": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "name": "Название контракта",
            "service": "Услуга",
            "file": "Файл контракта",
            "date_signed": "Дата заключения",
            "validity_period": "Период действия (в днях)",
            "amount": "Сумма",
        }
