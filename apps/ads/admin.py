from django.contrib import admin

from .models import Ad


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product", "channel", "budget")
    list_filter = ("channel", "budget")
    search_fields = ("name",)
    ordering = ("name",)
