from django.urls import path
from songs.views import song_list, song_info, add_song, delete_song, update_song,\
    author_list, author_info, add_author, update_author, delete_author, genre_list, \
    genre_info, add_genre, update_genre, delete_genre

urlpatterns = [
    path('', song_list, name='song_list'),
    path('about/<int:song_id>/', song_info, name='song_info'),
    path('add/', add_song, name='add_song'),
    path('remove/<int:song_id>/', delete_song, name='remove_song'),
    path('update/<int:song_id>/', update_song, name='update_song'),
    path('authors/', author_list, name='author_list'),
    path('authors/info/<int:author_id>/', author_info, name='author_info'),
    path('authors/add/', add_author, name='add_author'),
    path('authors/update/<int:author_id>/', update_author, name='update_author'),
    path('authors/remove/<int:author_id>/', delete_author, name='delete_author'),
    path('genres/', genre_list, name='genre_list'),
    path('genres/info/<int:genre_id>/', genre_info, name='genre_info'),
    path('genres/add/', add_genre, name='add_genre'),
    path('genres/update/<int:genre_id>/', update_genre, name='update_genre'),
    path('genres/remove/<int:genre_id>/', delete_genre, name='delete_genre'),
]
