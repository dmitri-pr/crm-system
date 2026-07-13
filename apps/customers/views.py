from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Customer
from .forms import CustomerCreateForm
from apps.contracts.models import Contract


class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = "customers-create.html"
    success_url = reverse_lazy("customers:list")

    def form_valid(self, form):
        self.object = form.save()  # noqa

        contract = form.cleaned_data["contract"]
        contract.customer = self.object
        contract.save()

        return super().form_valid(form)
