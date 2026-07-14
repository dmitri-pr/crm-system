from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerForm
from apps.contracts.models import Contract


class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers-list.html'
    context_object_name = 'customers'


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = 'customers-detail.html'
    context_object_name = 'object'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers-create.html"
    success_url = reverse_lazy("customers:list")


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers-edit.html'
    success_url = reverse_lazy('customers:list')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers-delete.html'
    success_url = reverse_lazy('customers:list')
