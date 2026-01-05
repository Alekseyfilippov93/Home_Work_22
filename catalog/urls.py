from django.urls import path
from catalog.views import ProductListView, ProductDetailView, ContactsTemplateView

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Слэш в конце!
]
# Все URL заканчиваются на '/' (согласно критериям задачи)
