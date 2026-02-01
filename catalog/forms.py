from django import forms
from catalog.models import Product

FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Исключаем владельца из формы, так как он ставится автоматически
        exclude = ("owner",)

    def __init__(self, *args, **kwargs):
        # Извлекаем пользователя из переданных аргументов
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        # 1. Стилизация
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"

        # 2. Логика прав доступа
        # Если пользователь модератор и НЕ владелец этого товара
        if (
            self.user
            and self.user.has_perm("catalog.can_unpublish_product")
            and self.instance.owner != self.user
        ):
            # Оставляем доступным только поле публикации
            for field_name in self.fields:
                if field_name != "is_published":
                    self.fields[field_name].disabled = True

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    f"Название содержит запрещенное слово: {word}"
                )
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in FORBIDDEN_WORDS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(
                    f"Описание содержит запрещенное слово: {word}"
                )
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price
