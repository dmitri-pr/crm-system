from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contract
from .forms import ContractCreateForm


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractCreateForm
    template_name = "contracts-create.html"
    success_url = reverse_lazy("contracts:list")
