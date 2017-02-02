from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *

class SongSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Song
    """
    # album= AlbumSerializer(read_only=True)

    class Meta:
        model = song_model.Song
        fields = ('id', 'title', 'song_length', 'release_date', 'artist', 'genre', 'album')
        depth = 1