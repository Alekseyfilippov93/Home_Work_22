from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1. Удаляем всё из базы данных
        # Сначала продукты
        Product.objects.all().delete()
        # Потом категории
        Category.objects.all().delete()

        # 2. Загружаем данные из файлов (фикстур)
        call_command('loaddata', 'catalog/fixtures/category_data.json')
        call_command('loaddata', 'catalog/fixtures/product_data.json')

        print("База очищена, данные из фикстур загружены!")
