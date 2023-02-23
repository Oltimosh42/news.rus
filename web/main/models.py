from django.db import models
from django.urls import reverse


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')
    intro = models.CharField(max_length=255, verbose_name='Интро')
    photo = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='Фото', null=True)
    content = models.TextField(verbose_name='Текст статьи')
    time_add = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_all', kwargs={'art_slug': self.slug})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']