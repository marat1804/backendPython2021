"""
File describing views for songs app
"""
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def song_list(request):
    """
    View for getting song list
    """
    return JsonResponse({'songs': [
        {
            'song_id': 1,
            'author': 'nothing.nowhere',
            'song_name': 'fake friend',
            'year': 2020
        },
        {
            'song_id': 2,
            'author': 'Imagine Dragons',
            'song_name': 'Thunder',
            'year': 2017
        },
    ]})


names = ['Blue', 'Apple', 'Pear', 'Horse', 'Cloud', 'Nine', 'Seven', 'Hair']
years = list(range(1990, 2022))


@require_GET
def song_info(request, song_id):
    """
    View for getting song info
    """
    return JsonResponse({
        'song_id': song_id,
        'author': 'Super Author ' + str(song_id),
        'song_name': names[song_id % len(names)] + ' ' + names[song_id * 2 % len(names)],
        'year': years[song_id % len(years)]
    })


@require_POST
def add_song(request):
    """
    View for adding song
    """
    result_dict = {'song_id': random.randint(1, 100)}
    data = json.loads(request.body)
    result_dict.update(data)
    return JsonResponse(result_dict)
