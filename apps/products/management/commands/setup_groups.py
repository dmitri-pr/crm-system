from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создаёт преднастроенные группы (если они не существуют)'

    def handle(self, *args, **options):
        group_data = {
            'Оператор': ['view_lead', 'add_lead', 'change_lead', 'delete_lead', 'can_view_statistics'],
            'Маркетолог': ['view_product', 'add_product', 'change_product', 'delete_product',
                           'view_ad', 'add_ad', 'change_ad', 'delete_ad', 'can_view_statistics'],
            'Менеджер': ['view_contract', 'add_contract', 'change_contract', 'delete_contract',
                         'view_customer', 'add_customer', 'change_customer', 'delete_customer',
                         'view_lead', 'can_view_statistics'],
        }

        for group_name, codenames in group_data.items():
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'Создана группа "{group_name}"')
            else:
                self.stdout.write(f'Группа "{group_name}" уже существует, пропускаем')

            permissions = Permission.objects.filter(codename__in=codenames)
            group.permissions.set(permissions)

        self.stdout.write(self.style.SUCCESS('Готово!'))
