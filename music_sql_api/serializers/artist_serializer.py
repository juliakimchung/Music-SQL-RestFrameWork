from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Artist

    """

    class Meta:
        model = artist_model.Artist
        fields = ('id', 'url', 'name', 'gender')