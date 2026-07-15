from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.mixins import SuperuserPermissionRequiredMixin
from .models import Contract
from .forms import ContractForm


class ContractListView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Contract
    template_name = 'contracts-list.html'
    context_object_name = 'contracts'
    permission_required = 'contracts.view_contract'


class ContractDetailView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contracts-detail.html'
    context_object_name = 'object'
    permission_required = 'contracts.view_contract'


class ContractCreateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = "contracts-create.html"
    success_url = reverse_lazy("contracts:list")
    permission_required = 'contracts.add_contract'


class ContractUpdateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contracts-edit.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.change_contract'


class ContractDeleteView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Contract
    template_name = 'contracts-delete.html'
    success_url = reverse_lazy('contracts:list')
    permission_required = 'contracts.delete_contract'
