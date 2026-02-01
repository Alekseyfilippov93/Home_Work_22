from django.core.cache import cache
from catalog.models import Product
from config import settings


def get_products_by_category(category_id):
    """
    Возвращает список всех опубликованных продуктов для конкретной категории.
    Использует низкоуровневое кеширование.
    """
    if not settings.CACHE_ENABLED:
        # Если кеш выключен, просто тянем из БД
        return Product.objects.filter(category_id=category_id, is_published=True)

    # Формируем уникальный ключ для кеша на основе ID категории
    key = f"products_category_{category_id}"
    products = cache.get(key)

    if products is None:
        # Если в кеше пусто, берем данные из БД и сохраняем в кеш на 15 минут
        products = Product.objects.filter(category_id=category_id, is_published=True)
        cache.set(key, products, 60 * 15)

    return products
