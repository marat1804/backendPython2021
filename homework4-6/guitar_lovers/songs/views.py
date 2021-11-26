"""
File describing views for songs app
"""
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator

from application.views import login_required
from .models import Song, Author, Genre
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import SongSerializer, AuthorSerializer, GenreSerializer


@method_decorator(login_required, name='dispatch')
class SongViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Song.objects.all()
        serializer = SongSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Song.objects.all()
        song = get_object_or_404(queryset, pk=pk)
        serializer = SongSerializer(song)
        return Response(serializer.data)

    def create(self, request):
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Song.objects.all()
        song = get_object_or_404(queryset, pk=pk)
        serializer = SongSerializer(
            instance=song,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Song.objects.all()
        song = get_object_or_404(queryset, pk=pk)
        song_id = song.id
        song.delete()
        return Response(data={'id': song_id}, status=status.HTTP_200_OK)


@method_decorator(login_required, name='dispatch')
class AuthorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Author.objects.all()
        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        serializer = AuthorSerializer(
            instance=author,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Author.objects.all()
        author = get_object_or_404(queryset, pk=pk)
        author_id = author.id
        author.delete()
        return Response(data={'id': author_id}, status=status.HTTP_200_OK)


@method_decorator(login_required, name='dispatch')
class GenreViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Genre.objects.all()
        serializer = GenreSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, pk=pk)
        serializer = GenreSerializer(
            instance=genre,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = Genre.objects.all()
        genre = get_object_or_404(queryset, pk=pk)
        genre_id = genre.id
        genre.delete()
        return Response(data={'id': genre_id}, status=status.HTTP_200_OK)