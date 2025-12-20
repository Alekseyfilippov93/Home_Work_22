from django.core.management import BaseCommand, call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 1. Удаляем всё из базы данных
        # Сначала продукты
        Product.objects.all().delete()
        # Потом категории
        Category.objects.all().delete()

        # 2. Загружаем данные из фикстур
        try:
            call_command('loaddata', 'catalog/fixtures/category_data.json')
            self.stdout.write(self.style.SUCCESS('Категории успешно загружены'))

            # Теперь ПРОДУКТЫ
            call_command('loaddata', 'catalog/fixtures/product_data.json')
            self.stdout.write(self.style.SUCCESS('Продукты успешно загружены'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при загрузке: {e}'))

        self.stdout.write(self.style.SUCCESS('Данные успешно обновлены!'))
