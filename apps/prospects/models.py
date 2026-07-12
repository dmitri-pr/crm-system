from django.db import models


class Prospect(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(blank=True, verbose_name="Email")
    campaign = models.ForeignKey(
        "campaigns.Campaign",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prospects",
        verbose_name="Рекламная кампания"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.full_name
