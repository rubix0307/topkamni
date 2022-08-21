from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    slug = models.SlugField(verbose_name='Url', max_length=255, unique=True)
    is_show_in_main_navigation = models.BooleanField(verbose_name='В основной навигации', default=False)
    is_show_in_social_links = models.BooleanField(verbose_name='В доп. навигации', default=False)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']