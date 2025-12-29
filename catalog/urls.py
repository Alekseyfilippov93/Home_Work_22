from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    home,
    contacts,
    product_detail,
)  # Импортируем наши функции-контроллеры

app_name = CatalogConfig.name

urlpatterns = [
    # path('', ...) соответствует адресу 'http://127.0.0.1:8000/'
    # name='home' используется для ссылки на этот URL в шаблонах (например, {% url 'home' %})
    path("", home, name="home"),
    # path('contacts/', ...) соответствует адресу 'http://127.0.0.1:8000/contacts/'
    path("contacts/", contacts, name="contacts"),
    # path('product/<int:pk>/' Путь для страницы одного товара, принимающий pk
    path("products/<int:pk>/", product_detail, name="product_detail"),
]
# Все URL заканчиваются на '/' (согласно критериям задачи)
