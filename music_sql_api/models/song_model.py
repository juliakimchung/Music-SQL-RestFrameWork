from django.db import models
from .artist_model import Artist
from .genre_model import Genre
from .album_model import Album

class Song(models.Model):

    """Class to create a table representing a Song
    extension of models.Model

    Variables:
        gid: a name that associates a system user with other users sharing something in common 
        title: the name of the Song
        release_date: the date the song was released
        song_length: the length of the song duration

    """

    title = models.CharField(max_length=200, blank=True)
    song_length = models.IntegerField(default=0)
    release_date = models.DateTimeField()
    artist = models.ForeignKey(Artist, related_name='songs', on_delete=models.CASCADE )
    genre = models.ForeignKey(Genre, related_name="songs", on_delete=models.CASCADE)
    # artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    # album = models.ManyToManyField(Album)

    def __str__(self):
        """
        Method to create a string representing a Song Method
        Returns a string representation of the song's title field
        """
        return self.title

        class Meta:

        
            ordering = ('title',)


