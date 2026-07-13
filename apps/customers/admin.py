from django.contrib import admin
from .models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'converted_at')
    list_filter = ('converted_at',)
    search_fields = ('lead__last_name', 'lead__first_name', 'lead__middle_name')
    ordering = ('-converted_at',)
