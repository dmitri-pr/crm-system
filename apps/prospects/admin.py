from django.contrib import admin
from .models import Prospect


@admin.register(Prospect)
class ProspectAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'email', 'campaign')
    list_filter = ('campaign',)
    search_fields = ('full_name', 'phone', 'email')
    ordering = ('-created_at',)
