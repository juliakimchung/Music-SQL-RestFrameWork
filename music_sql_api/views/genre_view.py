from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import genre_serializer
from music_sql_api.models import *

class GenreViewSet(viewsets.ModelViewSet):

	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""

	queryset = genre_model.Genre.objects.all()
	serializer_class = genre_serializer.GenreSerializer
