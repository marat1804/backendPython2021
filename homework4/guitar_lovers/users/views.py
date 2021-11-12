"""
File describing users app views
"""
import json
import random

from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import User
from django.http import HttpResponseNotFound, HttpResponseBadRequest


@require_GET
def user_list(request):
    """
    View for getting user list
    """
    return JsonResponse(
        {'users':
         [
             {'id': u.id,
              'username': u.username}
             for u in User.objects.all()
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
    form = json.loads(request.body)
    user = User()
    if 'first_name' not in form:
        return HttpResponseBadRequest("Field first_name is required")
    user.name = form.get('first_name')
    if 'last_name' not in form:
        return HttpResponseBadRequest("Field last_name is required")
    user.last_name = form.get('last_name')
    if 'username' not in form:
        return HttpResponseBadRequest("Field username is required")
    user.username = form.get('username')
    if 'email' not in form:
        return HttpResponseBadRequest("Field email is required")
    user.email = form.get('email')
    if 'bio' in form:
        user.bio = form.get('bio')
    if 'country' in form:
        user.country = form.get('country')
    if 'city' in form:
        user.city = form.get('city')
    if 'guitar' in form:
        user.guitar = form.get('guitar')
    user.save()
    return JsonResponse({'id': user.id})


@require_http_methods(['PATCH'])
def update_user(request, user_id):
    """
    View for updating a user
    """
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound('User not found')
    data = json.loads(request.body)
    if 'first_name' in data:
        user.first_name = data['first_name']
    if 'last_name' in data:
        user.last_name = data['last_name']
    if 'bio' in data:
        user.bio = data['bio']
    if 'country' in data:
        user.country = data['country']
    if 'city' in data:
        user.city = data['city']
    if 'last_name' in data:
        user.guitar = data['guitar']
    user.save()
    return JsonResponse({'updated': user_id})


@require_http_methods(['DELETE'])
def delete_user(request, user_id):
    """
    View for deleting user
    """
    try:
        User.objects.get(id=user_id)
    except User.DoesNotExist:
        return HttpResponseNotFound('User not found')

    User.objects.filter(id=user_id).delete()
    return JsonResponse({'deleted': user_id})
