from django.urls import path
from users.views import user_list, user_info, register_user, update_user, delete_user

urlpatterns = [
    path('', user_list, name='user_list'),
    path('profile/<int:user_id>/', user_info, name='user_info'),
    path('register/', register_user, name='register_user'),
    path('update/', update_user, name='update_user'),
    path('remove/', delete_user, name='delete_user'),
]
