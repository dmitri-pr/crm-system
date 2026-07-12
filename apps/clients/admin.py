from django.contrib import admin
from .models import ActiveClient


@admin.register(ActiveClient)
class ActiveClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'prospect', 'converted_at')
    list_filter = ('converted_at',)
    search_fields = ('prospect__full_name',)
    ordering = ('-converted_at',)
