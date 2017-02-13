from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *
from . import artist_serializer
class SongSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Song
    """
    # artist= artist_serializer.ArtistSerializer(read_only = True)
    

    class Meta:
        model = song_model.Song
        fields = ('id', 'title', 'song_length', 'release_date', 'artist', 'genre', 'album')
        # depth = 1