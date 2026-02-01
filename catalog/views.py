from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
)
from catalog.models import Product
from catalog.forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from catalog.services import get_products_by_category
from catalog.models import Category
from django.core.cache import cache
from config import settings


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"

    def get_queryset(self):
        """Реализация низкоуровневого кеширования списка продуктов"""
        # Сначала фильтруем только опубликованные
        queryset = super().get_queryset().filter(is_published=True)

        # Если кеш включен в settings.py
        if settings.CACHE_ENABLED:
            key = "all_products_list"  # Ключ для хранения в Redis
            cache_data = cache.get(key)

            if cache_data is None:
                # Если в кеше пусто, сохраняем туда QuerySet
                cache_data = queryset
                cache.set(key, cache_data, 60 * 15)  # Кешируем на 15 минут
            return cache_data

        return queryset


class ProductDetailView(DetailView, LoginRequiredMixin):
    model = Product
    template_name = "catalog/product_detail.html"


class ContactsTemplateView(TemplateView, LoginRequiredMixin):
    template_name = "catalog/contacts.html"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        # Сохраняем форму, но не фиксируем в БД
        product = form.save(commit=False)
        # Назначаем текущего пользователя владельцем
        product.owner = self.request.user
        # Теперь сохраняем окончательно
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        user = self.request.user
        product = self.get_object()

        # Правило: Владелец может всё, модератор — только если есть право
        if user == product.owner or user.has_perm("catalog.can_unpublish_product"):
            return True
        return False

    def get_form_kwargs(self):
        """Передает текущего пользователя в форму"""
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class ProductDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Product
    success_url = reverse_lazy("catalog:home")

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        # Удалять может владелец ИЛИ модератор с правом удаления
        if product.owner == user or user.has_perm("catalog.delete_product"):
            return True
        return False


class CategoryProductListView(ListView):
    model = Product
    template_name = "catalog/category_products.html"
    context_object_name = "products"

    def get_queryset(self):
        # Получаем id категории из URL и вызываем наш сервис
        category_id = self.kwargs.get("pk")
        return get_products_by_category(category_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавим название категории в заголовок страницы
        context["category"] = Category.objects.get(pk=self.kwargs.get("pk"))
        return context
