from rest_framework import viewsets
from django.contrib.auth.models import User
from music_sql_api.serializers import song_serializer
from music_sql_api.models import *
from rest_framework.response import Response
class SongViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provids 'list' and 'detail' actions.
    create method takes request as an argument which is to post data
    """
    queryset = song_model.Song.objects.all()
    serializer_class = song_serializer.SongSerializer
    def create(self, request):
        data=request.data
        artist = artist_model.Artist.objects.get_or_create(name = data["artist"])
        album = album_model.Album.objects.get_or_create(title = data["title"])
        genre = genre_model.Genre.objects.get_or_create(name = data["genre"])
        song = song_model.Song.objects.create(
            title = data["title"], 
            song_length = data["song_length"], 
            release_date = data["release_date"], 
            artist = artist[0],
            album = album[0], 
            genre = genre[0])

        return Response({'status': True})




        
        