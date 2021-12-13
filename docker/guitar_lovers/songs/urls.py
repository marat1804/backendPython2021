from django.urls import path
from songs.views import SongViewSet, AuthorViewSet, GenreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', SongViewSet, basename='songs')
router.register('authors', AuthorViewSet, basename='authors')
router.register('genres', GenreViewSet, basename='genres')

urlpatterns = router.urls
