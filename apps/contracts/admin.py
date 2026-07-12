from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'active_client', 'amount', 'date_signed')
    list_filter = ('service', 'active_client')
    search_fields = ('name',)
    ordering = ('-date_signed',)
