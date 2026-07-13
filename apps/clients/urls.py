from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('new/', views.ActiveClientCreateView.as_view(), name='create'),
]
