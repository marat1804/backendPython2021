"""
File describing views for songs app
"""
import json
import random
from .models import Song, Author, Genre
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseNotFound, HttpResponseBadRequest
from .forms import AddSongForm


@require_GET
def song_list(request):
    """
    View for getting song list
    """
    songs = Song.objects.all()
    data = [
        {
            'id': song.id,
            'name': song.name,
            'date': song.date,
            'author': song.author.name,
            'genre': song.genre_id.name
        } for song in songs
    ]
    return JsonResponse({'songs': data})


@require_GET
def song_info(request, song_id):
    """
    View for getting song info
    """
    try:
        song = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return HttpResponseNotFound(f'Not found song with id {song_id}')
    data = {
        'id': song.id,
        'name': song.name,
        'date': song.date,
        'author': song.author.name,
        'genre': song.genre_id.name
    }
    return JsonResponse(data)


@require_POST
def add_song(request):
    """
    View for adding song
    """
    form = json.loads(request.body)
    song = Song()

    song.name = form.get('name', None)
    if song.name is None:
        return HttpResponseBadRequest("Field name is required")
    if 'genre_id' not in form:
        return HttpResponseBadRequest("Field genre_id is required")
    genre_id = form.get('genre_id', None)
    try:
        genre = Genre.objects.get(id=genre_id)
        song.genre_id = genre
    except Genre.DoesNotExist:
        return HttpResponseNotFound(f'Genre with id = {genre_id} not found')
    if 'author' not in form:
        return HttpResponseBadRequest("Field author_id is required")
    author = form.get('author_id', None)
    try:
        author = Author.objects.get(id=author)
        song.author = author
    except Author.DoesNotExist:
        return HttpResponseNotFound(f'Author with id = {author} not found')
    if 'date' in form:
        song.date = form.get('date')
    if 'text' in form:
        song.text = form.get('text')
    song.save()
    return JsonResponse({'id': song.id})


@require_POST
def update_song(request, song_id):
    try:
        song = Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return HttpResponseNotFound('Song not found')
    data = json.loads(request.body)
    if 'name' in data:
        song.name = data['name']
    if 'text' in data:
        song.text = data['text']
    if 'genre_id' in data:
        try:
            genre = Genre.objects.get(id=data['genre_id'])
            song.genre_id = genre
        except Genre.DoesNotExist:
            return HttpResponseNotFound(f'Genre with id = {data["genre_id"]} not found')
    if 'date' in data:
        song.date = data['date']
    if 'author' in data:
        try:
            author = Author.objects.get(id=data['author'])
            song.author = author
        except Author.DoesNotExist:
            return HttpResponseNotFound(f'Author with id = {data["author"]} not found')

    song.save()
    return JsonResponse({'updated': song_id})


@require_POST
def delete_song(request, song_id):
    """
    View for deleting song
    """
    try:
        Song.objects.get(id=song_id)
    except Song.DoesNotExist:
        return HttpResponseNotFound('Song not found')

    Song.objects.filter(id=song_id).delete()
    return JsonResponse({'deleted': song_id})

