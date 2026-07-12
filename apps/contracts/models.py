from django.db import models


class Contract(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название контракта"
    )
    service = models.ForeignKey(
        "services.Service",
        on_delete=models.PROTECT,
        related_name="contracts",
        verbose_name="Услуга"
    )
    file = models.FileField(
        upload_to="contracts/",
        verbose_name="Файл контракта"
    )
    date_signed = models.DateField(verbose_name="Дата заключения")
    validity_period = models.DurationField(verbose_name="Период действия")
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма"
    )
    active_client = models.ForeignKey(
        "clients.ActiveClient",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contracts",
        verbose_name="Активный клиент"
    )

    def __str__(self):
        return self.name
