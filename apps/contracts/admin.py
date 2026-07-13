from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product', 'cost', 'customer', 'start_date', 'end_date')
    list_filter = ('product', 'customer')
    search_fields = ('name',)
    ordering = ('-start_date',)
