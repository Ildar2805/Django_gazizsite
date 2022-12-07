from django.db import models
from django.urls import reverse
import uuid


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL') #db_index чтобы поиск происходил побыстрее
    content = models.TextField(blank=True, verbose_name='Содержание') #может быть пустым
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Фото')
    source = models.URLField(blank=True, verbose_name='Источник')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey('Category', related_name='posts', verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    #Если url связаны с записями из БД, то лучше так, чем {% url 'post' post.pk %} + в Admin панели появляется ссылка на сайт
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-time_create']


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'