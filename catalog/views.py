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


class ProductListView(ListView):
    model = Product
    template_name = "catalog/home.html"


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
