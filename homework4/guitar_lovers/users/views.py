import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def user_list(request):
    return JsonResponse({'users': [
        {
            'user_id': 1,
            'username': 'user01'
        },
        {
            'user_id': 2,
            'username': 'user02'
        },
    ]})


names = ['John', 'Mike', 'Max', 'Lewis']
surnames = ['Green', 'Verstappen', 'Leclerc', 'Norris']


@require_GET
def user_info(request, pk):
    return JsonResponse({
        'user_id': pk,
        'username': 'unique_username_' + str(pk),
        'first_name': surnames[pk % len(surnames)],
        'second_name': names[pk % len(names)]
    })


@require_POST
def register_user(request):
    result_dict = {'user_id': random.randint(1, 100)}
    data = json.loads(request.body)
    result_dict.update(data)
    return JsonResponse(result_dict)

