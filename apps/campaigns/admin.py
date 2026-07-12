from django.contrib import admin

from .models import Campaign


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'service', 'channel', 'budget')
    list_filter = ('channel', 'budget')
    search_fields = ('name',)
    ordering = ('name',)
