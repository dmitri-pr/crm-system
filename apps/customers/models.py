from django.db import models


class Customer(models.Model):
    lead = models.OneToOneField(
        'leads.Lead',
        on_delete=models.CASCADE,
        related_name="customer",
        verbose_name="Клиент"
    )
    converted_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата перевода")

    def __str__(self):
        return f"{self.lead.last_name} {self.lead.first_name} {self.lead.middle_name or ''}".strip()
