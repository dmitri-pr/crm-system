from django.db import models


class Contract(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название контракта"
    )
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.PROTECT,
        related_name="contracts",
        verbose_name="Услуга"
    )
    file = models.FileField(
        upload_to="contracts/",
        verbose_name="Файл контракта"
    )
    start_date = models.DateField(verbose_name="Дата заключения")
    end_date = models.DateField(verbose_name="Дата истечения")
    cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Сумма"
    )
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="contracts",
        verbose_name="Активный клиент"
    )

    def __str__(self) -> str:
        return self.name
