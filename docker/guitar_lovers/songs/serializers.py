from .models import Song, Author, Genre
from rest_framework import serializers
from django.utils.timezone import now


class SongSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        required=True,
        slug_field='name',
    )
    genre_id = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        required=True,
        slug_field='name',
    )

    def validate(self, data):
        if not data.get('date'):
            return data
        if data['date'] > now().date():
            raise serializers.ValidationError('Date cannot be from future')
        return data

    class Meta:
        model = Song
        fields = ['id', 'name', 'date', 'text', 'genre_id', 'author']


class AuthorSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'country', 'record_label']


class GenreSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Genre
        fields = ['id', 'name']
