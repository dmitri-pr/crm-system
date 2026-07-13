from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import ActiveClient
from .forms import ActiveClientCreateForm
from apps.contracts.models import Contract


class ActiveClientCreateView(LoginRequiredMixin, CreateView):
    model = ActiveClient
    form_class = ActiveClientCreateForm
    template_name = "customers-create.html"
    success_url = reverse_lazy("clients:list")

    def form_valid(self, form):
        self.object = form.save()

        contract = form.cleaned_data["contract"]
        contract.active_client = self.object
        contract.save()

        return super().form_valid(form)
