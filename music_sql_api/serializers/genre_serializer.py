from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *

class GenreSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = genre_model.Genre
        fields = ('id', 'url', 'name')
