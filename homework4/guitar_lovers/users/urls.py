from django.urls import path
from users.views import user_list, user_info, register_user

urlpatterns = [
    path('', user_list, name='user_list'),
    path('profile/<int:user_id>/', user_info, name='user_info'),
    path('register/', register_user, name='register_user'),
]
