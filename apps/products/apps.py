from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.products"
    verbose_name = "Услуги"

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.core.management import call_command

        def create_groups(sender, **kwargs):
            call_command("setup_groups", verbosity=0)

        post_migrate.connect(create_groups, sender=self)
