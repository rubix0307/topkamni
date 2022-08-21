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


class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(verbose_name='Фото', blank=True, upload_to='photo/%Y/%m/')
    category = models.ForeignKey(Category,
                                verbose_name='Категория',
                                on_delete=models.PROTECT,
                                null=True,
                                )
    is_published = models.BooleanField(verbose_name='Опубликовано', default=False, blank=True,)
    views = models.IntegerField(verbose_name='Просмотры',default=0)
    update_date = models.DateTimeField(verbose_name='Время изменения', auto_now=True, blank=True,)
    create_date = models.DateTimeField(verbose_name='Время создания', auto_now_add=True, blank=True,)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})
    

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья(ю)'
        verbose_name_plural = 'Статьи'