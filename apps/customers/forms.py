from typing import Any

from django import forms
from apps.contracts.models import Contract
from ..ads.models import Ad
from .models import Customer


class CustomerCreateForm(forms.ModelForm):
    contract = forms.ModelChoiceField(
        queryset=Contract.objects.filter(customer__isnull=True),
        label="Контракт",
        required=True,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = Customer
        fields = ["lead"]
        widgets = {
            "lead": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "lead": "Потенциальный клиент",
        }

    def save(self, commit: bool = True) -> Customer:
        customer = super().save(commit=commit)
        contract = self.cleaned_data["contract"]
        contract.customer = customer
        contract.save()
        return customer


class CustomerUpdateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = []

    last_name = forms.CharField(
        max_length=100, label="Фамилия",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    first_name = forms.CharField(
        max_length=100, label="Имя",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    middle_name = forms.CharField(
        max_length=100, required=False, label="Отчество",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    phone = forms.CharField(
        max_length=20, label="Телефон",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )
    ad = forms.ModelChoiceField(
        queryset=Ad.objects.all(),
        label="Рекламная кампания",
        widget=forms.Select(attrs={"class": "form-select"})
    )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            lead = self.instance.lead
            self.fields["first_name"].initial = lead.first_name
            self.fields["last_name"].initial = lead.last_name
            self.fields["middle_name"].initial = lead.middle_name
            self.fields["phone"].initial = lead.phone
            self.fields["email"].initial = lead.email
            self.fields["ad"].initial = lead.ad

    def save(self, commit: bool = True) -> Customer:
        customer = super().save(commit=False)
        lead = customer.lead
        lead.first_name = self.cleaned_data["first_name"]
        lead.last_name = self.cleaned_data["last_name"]
        lead.middle_name = self.cleaned_data["middle_name"]
        lead.phone = self.cleaned_data["phone"]
        lead.email = self.cleaned_data["email"]
        lead.ad = self.cleaned_data["ad"]
        if commit:
            lead.save()
            customer.save()
        return customer
