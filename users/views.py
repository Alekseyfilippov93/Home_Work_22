from django.urls import reverse_lazy
from django.views.generic import CreateView
from users.models import User
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        # Отправка приветственного письма
        send_mail(
            subject="Добро пожаловать в наш магазин!",
            message="Вы успешно зарегистрировались на платформе Skystore.",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)
