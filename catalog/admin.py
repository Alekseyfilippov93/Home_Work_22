from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Отображение id и наименования в списке
    list_display = ('id', 'name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Колонки, которые будут видны в списке товаров
    list_display = ('id', 'name', 'price', 'category',)

    # Фильтрация по категории (справа появится панель фильтров)
    list_filter = ('category',)

    # Поиск по названию и описанию
    search_fields = ('name', 'description',)
