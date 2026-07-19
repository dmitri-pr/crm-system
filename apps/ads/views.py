from typing import Any, Dict
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Sum

from core.mixins import SuperuserPermissionRequiredMixin
from .models import Ad
from .forms import AdForm


class AdListView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = Ad
    template_name = "ads-list.html"
    context_object_name = "ads"
    permission_required = "ads.view_ad"


class AdDetailView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DetailView):
    model = Ad
    template_name = "ads-detail.html"
    context_object_name = "object"
    permission_required = "ads.view_ad"


class AdCreateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Ad
    form_class = AdForm
    template_name = "ads-create.html"
    success_url = reverse_lazy("ads:list")
    permission_required = "ads.add_ad"


class AdUpdateView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Ad
    form_class = AdForm
    template_name = "ads-edit.html"
    success_url = reverse_lazy("ads:list")
    permission_required = "ads.change_ad"


class AdDeleteView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Ad
    template_name = "ads-delete.html"
    success_url = reverse_lazy("ads:list")
    permission_required = "ads.delete_ad"


class AdStatisticView(SuperuserPermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "ads-statistic.html"
    permission_required = "ads.can_view_statistics"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        ads = Ad.objects.annotate(
            leads_count=Count("leads", distinct=True),
            customers_count=Count("leads__customer", distinct=True),
            total_revenue=Sum("leads__customer__contracts__cost", distinct=True)
        )

        for ad in ads:
            if ad.budget > 0:
                ad.profit = ((ad.total_revenue or 0) - ad.budget) / ad.budget * 100  # type: ignore[attr-defined]
            else:
                ad.profit = None  # type: ignore[attr-defined]

        context["ads"] = ads
        return context
