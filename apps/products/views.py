from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.mixins import SuperuserPermissionRequiredMixin
from .models import Product
from .forms import ProductForm


class ProductListView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products-list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'


class ProductDetailView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'products-detail.html'
    context_object_name = 'object'
    permission_required = 'products.view_product'


class ProductCreateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products-create.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.add_product'


class ProductUpdateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products-edit.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.change_product'


class ProductDeleteView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products-delete.html'
    success_url = reverse_lazy('products:list')
    permission_required = 'products.delete_product'
