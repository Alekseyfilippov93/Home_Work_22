from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Критерий 8: Только опубликованные статьи"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Критерий 8: Увеличение счетчика просмотров"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        "title",
        "content",
        "image",
        "is_published",
    )
    success_url = reverse_lazy("blog:list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        "title",
        "content",
        "image",
        "is_published",
    )

    def get_success_url(self):
        """Критерий 8: Перенаправление на саму статью после редактирования"""
        return reverse("blog:view", kwargs={"pk": self.object.pk})


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:list")
