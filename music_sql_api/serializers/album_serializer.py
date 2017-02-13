from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *
from . import song_serializer

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Album
    """
    songs = song_serializer.SongSerializer(many=True, read_only=True)

    class Meta:
        model = album_model.Album
        fields = ('id', 'url', 'title','label', 'album_length', 'release_date', 'songs')
        