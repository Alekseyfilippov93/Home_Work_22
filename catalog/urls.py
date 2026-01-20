from django.urls import path
from catalog.views import (
    ProductListView,
    ProductDetailView,
    ContactsTemplateView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="home"),
    path("contacts/", ContactsTemplateView.as_view(), name="contacts"),
    path(
        "products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),  # Слэш в конце!
    # Новые маршруты
    path("create/", ProductCreateView.as_view(), name="product_create"),
    path("edit/<int:pk>/", ProductUpdateView.as_view(), name="product_edit"),
    path("delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
]
# Все URL заканчиваются на '/' (согласно критериям задачи)
