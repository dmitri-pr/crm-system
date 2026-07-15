from django.urls import path
from . import views

app_name = 'ads'

urlpatterns = [
    path('', views.AdListView.as_view(), name='list'),
    path('new/', views.AdCreateView.as_view(), name='create'),
    path('statistic/', views.AdStatisticView.as_view(), name='statistic'),
    path('<int:pk>/', views.AdDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.AdUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.AdDeleteView.as_view(), name='delete'),
    # path('statistic/', views.AdStatisticView.as_view(), name='statistic'),
]
