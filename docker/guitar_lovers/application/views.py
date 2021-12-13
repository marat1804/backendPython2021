from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET


def login_required(function):
    def check_authenticate(*args, **kwargs):
        if len(args) > 1:
            request = args[1]
        else:
            request = args[0]

        if request.user.is_authenticated:
            return function(*args, **kwargs)
        else:
            return redirect('login')

    return check_authenticate


@login_required
@require_GET
def index_page(request):
    return render(request, 'index.html', {
        'name': request.user.first_name,
        'surname': request.user.last_name})


def login(request):
    return render(request, 'login.html')