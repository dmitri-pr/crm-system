from typing import Dict, Any
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.mixins import SuperuserPermissionRequiredMixin
from .models import Customer
from .forms import CustomerForm


class CustomerListView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers-list.html'
    context_object_name = 'customers'
    permission_required = 'customers.view_customer'


class CustomerDetailView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers-detail.html'
    context_object_name = 'object'
    permission_required = 'customers.view_customer'


class CustomerCreateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers-create.html"
    success_url = reverse_lazy("customers:list")
    permission_required = 'customers.add_customer'

    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        lead_id = self.request.GET.get('lead')
        if lead_id:
            initial['lead'] = lead_id
        return initial


class CustomerUpdateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers-edit.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.change_customer'


class CustomerDeleteView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers-delete.html'
    success_url = reverse_lazy('customers:list')
    permission_required = 'customers.delete_customer'
