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
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView, LoginRequiredMixin):
    model = Product
    template_name = "catalog/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
