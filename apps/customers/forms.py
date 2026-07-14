from django import forms
from .models import Customer
from apps.contracts.models import Contract
from apps.leads.models import Lead


class CustomerForm(forms.ModelForm):
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

    def save(self, commit=True):
        customer = super().save(commit=commit)
        contract = self.cleaned_data['contract']
        contract.customer = customer
        contract.save()
        return customer
