from django.core.mail import send_mail
from django.utils import timezone
from celery import shared_task

from application import settings


@shared_task()
def new_song(song_artist, song_title, who):
    send_mail(
        subject='SongDB notification',
        message=f'New song {song_artist} - {song_title} added by {who}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.ADMIN_EMAIL],
    )


@shared_task
def count_task():
    from users.models import User
    with open(settings.CELERY_LOG_FILE, 'a') as f:
        count = len(User.objects.all())
        f.write(f'{timezone.now()}: {count}\n')
