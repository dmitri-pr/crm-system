from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from core.mixins import SuperuserPermissionRequiredMixin
from .models import Lead
from .forms import LeadForm


class LeadListView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'leads-list.html'
    context_object_name = 'leads'
    permission_required = 'leads.view_lead'


class LeadDetailView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Lead
    template_name = 'leads-detail.html'
    context_object_name = 'object'
    permission_required = 'leads.view_lead'


class LeadCreateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads-create.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.add_lead'


class LeadUpdateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Lead
    form_class = LeadForm
    template_name = 'leads-edit.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.change_lead'


class LeadDeleteView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Lead
    template_name = 'leads-delete.html'
    success_url = reverse_lazy('leads:list')
    permission_required = 'leads.delete_lead'
