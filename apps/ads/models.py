from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название кампании")
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="ads",
        verbose_name="Рекламируемая услуга"
    )
    channel = models.CharField(
        max_length=100,
        verbose_name="Канал продвижения"
    )
    budget = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Бюджет"
    )

    class Meta:
        permissions = [
            ("can_view_statistics", "Может просматривать статистику рекламных кампаний"),
        ]

    def __str__(self):
        return self.name
