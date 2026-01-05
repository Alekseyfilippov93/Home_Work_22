from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='превью', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блоговая запись'
        verbose_name_plural = 'блоговые записи'
