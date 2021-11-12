from django.contrib import admin
from .models import Author, Genre, Song


class SongAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre_id', 'author_id')
    list_filter = ['date']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['record_label']


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Song, SongAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
