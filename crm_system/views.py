from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

from apps.products.models import Product
from apps.ads.models import Ad
from apps.leads.models import Lead
from apps.customers.models import Customer


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['products_count'] = Product.objects.count()
        context['ads_count'] = Ad.objects.count()
        context['leads_count'] = Lead.objects.count()
        context['customers_count'] = Customer.objects.count()

        return context
