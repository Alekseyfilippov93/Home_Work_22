from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")
        ct = ContentType.objects.get_for_model(Product)

        # Отмена публикаций и удаление
        perms = [
            Permission.objects.get(codename="can_unpublish_product", content_type=ct),
            Permission.objects.get(codename="delete_product", content_type=ct),
        ]

        group.permissions.add(*perms)
        self.stdout.write(self.style.SUCCESS("Группа настроена"))
