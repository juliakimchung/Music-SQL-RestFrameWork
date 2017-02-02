from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.models import *
from music_sql_api.serializers import album_serializer

class AlbumViewSet(viewsets.ModelViewSet):

	queryset = album_model.Album.objects.all()
	serializer_class = album_serializer.AlbumSerializer