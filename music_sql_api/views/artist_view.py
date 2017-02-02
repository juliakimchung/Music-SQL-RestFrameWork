from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import artist_serializer
from music_sql_api.models import *

class ArtistViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""
	queryset = artist_model.Artist.objects.all()
	serializer_class = artist_serializer.ArtistSerializer
