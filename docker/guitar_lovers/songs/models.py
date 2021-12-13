from datetime import datetime
from django.utils import timezone
from django.db import models

DEFAULT_LENGTH = 64


class Author(models.Model):
    name = models.CharField(
        max_length=DEFAULT_LENGTH,
        verbose_name='Имя исполнителя',
        unique=True
    )
    country = models.CharField(
        max_length=DEFAULT_LENGTH,
        verbose_name='Страна'
    )
    record_label = models.CharField(
        max_length=DEFAULT_LENGTH,
        null=True,
        verbose_name='Звукозаписывающий лейбл'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Genre(models.Model):
    name = models.CharField(
        max_length=DEFAULT_LENGTH,
        unique=True,
        verbose_name='Жанр'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Song(models.Model):
    name = models.CharField(
        max_length=DEFAULT_LENGTH,
        verbose_name='Название песни'
    )
    date = models.DateField(
        verbose_name='Дата выхода',
        null=True,
        default=timezone.now().date()
    )
    text = models.CharField(
        max_length=1024,
        verbose_name='Текст песни',
        null=True
    )
    genre_id = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='songs',
        verbose_name='Id жанра'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='songs',
        verbose_name='Id исполнителя'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Песня'
        verbose_name_plural = 'Песни'

