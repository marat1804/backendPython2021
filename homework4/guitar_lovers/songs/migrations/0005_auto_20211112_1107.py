# Generated by Django 3.2.9 on 2021-11-12 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_auto_20211112_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['name'], 'verbose_name': 'Исполнитель', 'verbose_name_plural': 'Исполнители'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['name'], 'verbose_name': 'Песня', 'verbose_name_plural': 'Песни'},
        ),
    ]