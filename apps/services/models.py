from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название услуги")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")

    def __str__(self):
        return self.name
