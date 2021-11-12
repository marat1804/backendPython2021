"""
File describing views for songs app
"""
import json
from .models import Song, Author, Genre
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import HttpResponseNotFound, HttpResponseBadRequest


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
        'genre': song.genre_id.name,
        'text': song.text
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
    if 'author_id' not in form:
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


@require_http_methods(['PATCH'])
def update_song(request, song_id):
    """
    View for updating a song
    """
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


@require_http_methods(['DELETE'])
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


@require_GET
def author_list(request):
    """
    View for getting author list
    """
    authors = Author.objects.all()
    data = [
        {
            'id': author.id,
            'name': author.name,
            'country': author.country,
            'record_label': author.record_label
        } for author in authors
    ]
    return JsonResponse({'authors': data})


@require_GET
def author_info(request, author_id):
    """
    View for getting author info
    """
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponseNotFound(f'Not found author with id {author_id}')
    data = {
        'id': author.id,
        'name': author.name,
        'country': author.country,
        'record_label': author.record_label
    }
    return JsonResponse(data)


@require_POST
def add_author(request):
    """
    View for adding author
    """
    form = json.loads(request.body)
    author = Author()
    if 'name' not in form:
        return HttpResponseBadRequest("Field name is required")
    author.name = form.get('name')
    if 'country' not in form:
        return HttpResponseBadRequest("Field country is required")
    author.country = form.get('country')
    if 'record_label' in form:
        author.record_label = form.get('record_label')
    author.save()
    return JsonResponse({'id': author.id})


@require_http_methods(['PATCH'])
def update_author(request, author_id):
    """
    View for updating a author
    """
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponseNotFound('Author not found')
    data = json.loads(request.body)
    if 'name' in data:
        author.name = data['name']
    if 'country' in data:
        author.country = data['country']
    if 'record_label' in data:
        author.record_label = data['record_label']

    author.save()
    return JsonResponse({'updated': author_id})


@require_http_methods(['DELETE'])
def delete_author(request, author_id):
    """
    View for deleting song
    """
    try:
        Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        return HttpResponseNotFound('Author not found')

    Author.objects.filter(id=author_id).delete()
    return JsonResponse({'deleted': author_id})


@require_GET
def genre_list(request):
    """
    View for getting genre list
    """
    genres = Genre.objects.all()
    data = [
        {
            'id': genre.id,
            'name': genre.name
        } for genre in genres
    ]
    return JsonResponse({'authors': data})


@require_GET
def genre_info(request, genre_id):
    """
    View for getting genre info
    """
    try:
        genre = Genre.objects.get(id=genre_id)
    except Genre.DoesNotExist:
        return HttpResponseNotFound(f'Not found genre with id {genre_id}')
    data = {
        'id': genre.id,
        'name': genre.name
    }
    return JsonResponse(data)


@require_POST
def add_genre(request):
    """
    View for adding genre
    """
    form = json.loads(request.body)
    genre = Genre()
    if 'name' not in form:
        return HttpResponseBadRequest("Field name is required")
    genre.name = form.get('name')
    genre.save()
    return JsonResponse({'id': genre.id})


@require_http_methods(['PATCH'])
def update_genre(request, genre_id):
    """
    View for updating a genre
    """
    try:
        genre = Genre.objects.get(id=genre_id)
    except Genre.DoesNotExist:
        return HttpResponseNotFound('Genre not found')
    data = json.loads(request.body)
    if 'name' in data:
        genre.name = data['name']
    genre.save()
    return JsonResponse({'updated': genre_id})


@require_http_methods(['DELETE'])
def delete_genre(request, genre_id):
    """
    View for deleting song
    """
    try:
        Genre.objects.get(id=genre_id)
    except Genre.DoesNotExist:
        return HttpResponseNotFound('Genre not found')

    Genre.objects.filter(id=genre_id).delete()
    return JsonResponse({'deleted': genre_id})
