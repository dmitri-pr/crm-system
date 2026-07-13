from django.urls import path
from . import views

app_name = "contracts"

urlpatterns = [
    path("new/", views.ContractCreateView.as_view(), name="create"),
]
