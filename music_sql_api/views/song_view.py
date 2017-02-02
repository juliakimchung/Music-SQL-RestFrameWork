from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import song_serializer
from music_sql_api.models import *

class SongViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provids 'list' and 'detail' actions.
	"""
	queryset = song_model.Song.objects.all()
	serializer_class = song_serializer.SongSerializer