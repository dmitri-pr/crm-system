from django.db import models


class ActiveClient(models.Model):
    prospect = models.OneToOneField(
        'prospects.Prospect',
        on_delete=models.CASCADE,
        related_name="active_client",
        verbose_name="Клиент"
    )
    converted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата перевода")

    def __str__(self):
        return self.prospect.full_name

