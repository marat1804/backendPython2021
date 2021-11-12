from django.contrib import admin
from .models import Author, Genre, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre_id', 'author_id')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Song, SongAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
