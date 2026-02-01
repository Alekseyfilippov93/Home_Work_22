from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    image = models.ImageField(
        upload_to="products/", verbose_name="Изображение", blank=True, null=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="products",
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )

    # auto_now_add устанавливает дату при создании
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # auto_now обновляет дату при каждом сохранении (изменении)
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        blank=True,
        null=True,
    )

    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at"]  # Сортировка: новые сверху
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return f"{self.name} ({self.price})"
