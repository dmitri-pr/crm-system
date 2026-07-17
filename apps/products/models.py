from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(blank=True, verbose_name="Описание")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self) -> str:
        return self.name
