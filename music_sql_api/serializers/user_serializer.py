from django.contrib.auth.models import User
from rest_framework import serializers
from music_sql_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', "first_name", "last_name")
