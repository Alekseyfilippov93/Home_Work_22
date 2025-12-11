from django.urls import path
from catalog.views import home, contacts  # Импортируем наши функции-контроллеры

urlpatterns = [
    # path('', ...) соответствует адресу 'http://127.0.0.1:8000/'
    # name='home' используется для ссылки на этот URL в шаблонах (например, {% url 'home' %})
    path("", home, name="home"),
    # path('contacts/', ...) соответствует адресу 'http://127.0.0.1:8000/contacts/'
    path("contacts/", contacts, name="contacts"),
]
# Все URL заканчиваются на '/' (согласно критериям задачи)
