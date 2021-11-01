import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def song_list(request):
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
def song_info(request, pk):
    return JsonResponse({
        'song_id': pk,
        'author': 'Super Author ' + str(pk),
        'song_name': names[pk % len(names)] + ' ' + names[pk * 2 % len(names)],
        'year': years[pk % len(years)]
    })


@require_POST
def add_song(request):
    result_dict = {'song_id': random.randint(1, 100)}
    data = json.loads(request.body)
    result_dict.update(data)
    return JsonResponse(result_dict)

