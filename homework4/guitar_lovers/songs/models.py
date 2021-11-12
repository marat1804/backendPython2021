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


class Genre(models.Model):
    name = models.CharField(
        max_length=DEFAULT_LENGTH,
        unique=True,
        verbose_name='Жанр'
    )


class Song(models.Model):
    name = models.CharField(
        max_length=DEFAULT_LENGTH,
        verbose_name='Название песни'
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата выхода',
        null=True
    )
    text = models.CharField(
        max_length=1024,
        verbose_name='Текст песни'
    )
    genre_id = models.ForeignKey(
        Genre,
        null=True,
        on_delete=models.SET_NULL,
        related_name='songs'
    )
    author_id = models.ManyToManyField(
        Author,
        related_name='songs'
    )

