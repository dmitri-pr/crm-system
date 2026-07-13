from django.urls import path
from . import views

app_name = 'customers'

urlpatterns = [
    path('new/', views.CustomerCreateView.as_view(), name='create'),
]
