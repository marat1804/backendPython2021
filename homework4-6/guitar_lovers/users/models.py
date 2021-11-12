from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    bio = models.TextField(
        verbose_name='О себе',
        max_length=100,
        blank=True
    )
    country = models.CharField(
        verbose_name='Страна',
        max_length=50,
        blank=True
    )
    city = models.CharField(
        verbose_name='Город',
        max_length=50,
        blank=True
    )
    guitar = models.CharField(
        verbose_name='Гитара',
        max_length=100,
        blank=True
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
