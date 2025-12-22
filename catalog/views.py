from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    """
    Контроллер для отображения главной страницы (Каталог).
    Рендерит шаблон home.html.
    """
    products_list = Product.objects.all()
    context = {"object_list": products_list, "title": "Главная страница"}
    # Django автоматически ищет 'home.html' в catalog/templates/

    return render(request, "home.html", context)


def product_detail(request, pk):
    """
    Контроллер для отображения страницы одного товара.
    Принимает pk (первичный ключ) товара.
    """
    # ORM-запрос: получаем объект по pk или выдаем 404
    product = get_object_or_404(Product, pk=pk)

    context = {"object": product, "title": product.name}
    return render(request, "product_detail.html", context)


def contacts(request):
    """
    Контроллер для отображения страницы контактов.
    Рендерит шаблон contacts.html.
    """
    return render(request, "contacts.html")
