from django.urls import path
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    CategoryProductListView,
)

from django.views.decorators.cache import cache_page

app_name = "catalog"

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "products/<int:pk>/",
        cache_page(60 * 15)(ProductDetailView.as_view()),
        name="product_detail",
    ),  # Слэш в конце! + Кешируем страницу товара на 15 минут (60 сек * 15)
    # Новые маршруты
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path(
        "category/<int:pk>/",
        CategoryProductListView.as_view(),
        name="category_products",
    ),
]
# Все URL заканчиваются на '/' (согласно критериям задачи)
