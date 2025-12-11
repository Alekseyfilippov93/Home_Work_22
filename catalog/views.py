from django.shortcuts import render


def home(request):
    """
    Контроллер для отображения главной страницы (Каталог).
    Рендерит шаблон home.html.
    """
    # Django автоматически ищет 'home.html' в catalog/templates/
    return render(request, "home.html")


def contacts(request):
    """
    Контроллер для отображения страницы контактов.
    Рендерит шаблон contacts.html.
    """
    return render(request, "contacts.html")
