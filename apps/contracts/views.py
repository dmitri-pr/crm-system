from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Contract
from .forms import ContractForm


class ContractListView(LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts-list.html'
    context_object_name = 'contracts'


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts-detail.html'
    context_object_name = 'object'


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts-create.html"
    success_url = reverse_lazy("contracts:list")


class ContractUpdateView(LoginRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts-edit.html'
    success_url = reverse_lazy('contracts:list')


class ContractDeleteView(LoginRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts-delete.html'
    success_url = reverse_lazy('contracts:list')
