from rest_framework import serializers
from music_sql_api.models import *
from django.contrib.auth import models
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', "first_name", "last_name")

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Artist

    """

    class Meta:
        model = Artist
        fields = ('id', 'url', 'name', 'gender')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Album
    """

    class Meta:
        model = Album
        fields = ('id', 'url', 'title','label', 'album_length', 'release_date', )
class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Genre
        fields = ('id', 'url', 'name')

class SongSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Song
    """
    # album= AlbumSerializer(read_only=True)

    class Meta:
        model = Song
        fields = ('id', 'title', 'song_length', 'release_date', 'artist', 'genre', 'album')
        depth = 1



