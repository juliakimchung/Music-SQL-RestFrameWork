from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import *


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer 


class AlbumViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provids 'list' and 'detail' actions.
	"""

	queryset = Album.objects.all()
	serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provids 'list' and 'detail' actions.
	"""
	queryset = Song.objects.all()
	serializer_class = SongSerializer

class ArtistViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = Artist.objects.all()
	serializer_class = ArtistSerializer

class GenreViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""

	queryset = Genre.objects.all()
	serializer_class = GenreSerializer

# class AlbumSongViewSet(viewsets.ModelViewSet):

# 	queryset = AlbumSong.objects.all()
# 	serializer_class = AlbumSongSerializer

