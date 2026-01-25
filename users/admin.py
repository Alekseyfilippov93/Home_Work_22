from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Список полей, которые будут видны в таблице всех пользователей
    list_display = ("id", "email", "phone", "country", "is_staff")
    # Поля, по которым можно искать
    search_fields = (
        "email",
        "phone",
    )
