"""
File describing users app views
"""
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST


@require_GET
def user_list(request):
    """
    View for getting user list
    """
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
def user_info(request, user_id):
    """
    View for getting user info
    """
    return JsonResponse({
        'user_id': user_id,
        'username': 'unique_username_' + str(user_id),
        'first_name': surnames[user_id % len(surnames)],
        'second_name': names[user_id % len(names)]
    })


@require_POST
def register_user(request):
    """
    View for user register
    """
    result_dict = {'user_id': random.randint(1, 100)}
    data = json.loads(request.body)
    result_dict.update(data)
    return JsonResponse(result_dict)
