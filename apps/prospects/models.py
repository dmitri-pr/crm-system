# from django.db import models
# from apps.campaigns.models import Campaign
#
#
# class Prospect(models.Model):
#     full_name = models.CharField(max_length=255, verbose_name="Ф.И.О.")
#     phone = models.CharField(max_length=20, verbose_name="Телефон")
#     email = models.EmailField(verbose_name="Email")
#     campaign = models.ForeignKey(
#         Campaign,
#         on_delete=models.SET_NULL,
#         null=True,
#         verbose_name="Рекламная кампания"
#     )
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.full_name
