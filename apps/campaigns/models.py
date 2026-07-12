from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название кампании")
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.PROTECT,
        related_name="campaigns",
        verbose_name="Рекламируемая услуга"
    )
    channel = models.CharField(
        max_length=100,
        verbose_name="Канал продвижения"
    )
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет"
    )

    def __str__(self):
        return self.name

