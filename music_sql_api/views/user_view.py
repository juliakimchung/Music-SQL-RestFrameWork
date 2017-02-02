from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import user_serializer
# from music_sql_api.models import *


class UserViewSet(viewsets.ModelViewSet):
	"""
	This viewset automatically provides 'list' and 'detail' actions.
	"""

	queryset = User.objects.all()
	serializer_class = user_serializer.UserSerializer 