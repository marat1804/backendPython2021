from django.urls import path
from songs.views import song_list, song_info, add_song, delete_song, update_song

urlpatterns = [
    path('', song_list, name='song_list'),
    path('about/<int:song_id>/', song_info, name='song_info'),
    path('add/', add_song, name='add_song'),
    path('remove/<int:song_id>/', delete_song, name='remove_song'),
    path('update/<int:song_id>/', update_song, name='update_song'),
]
