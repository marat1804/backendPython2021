from django.urls import path
from songs.views import song_list, song_info, add_song

urlpatterns = [
    path('', song_list, name='song_list'),
    path('about/<int:song_id>/', song_info, name='song_info'),
    path('add/', add_song, name='add_song'),
]
