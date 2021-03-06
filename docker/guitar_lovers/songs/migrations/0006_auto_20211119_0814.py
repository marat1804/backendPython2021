# Generated by Django 3.2.9 on 2021-11-19 08:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20211112_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='songs.author', verbose_name='Id исполнителя'),
        ),
        migrations.AlterField(
            model_name='song',
            name='date',
            field=models.DateField(default=datetime.date(2021, 11, 19), null=True, verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='songs', to='songs.genre', verbose_name='Id жанра'),
        ),
    ]
