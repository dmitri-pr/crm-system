from django import forms
from .models import ActiveClient
from apps.contracts.models import Contract
from apps.prospects.models import Prospect


class ActiveClientCreateForm(forms.ModelForm):
    contract = forms.ModelChoiceField(
        queryset=Contract.objects.filter(active_client__isnull=True),
        label="Контракт",
        required=True,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = ActiveClient
        fields = ["prospect"]
        widgets = {
            "prospect": forms.Select(attrs={"class": "form-select"}),
        }
        labels = {
            "prospect": "Потенциальный клиент",
        }
