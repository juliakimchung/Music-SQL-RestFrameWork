from django.db import models

# Create your models here.
class Artist(models.Model):
    """Class to create a table representing a artist
    extension of models.Model

    Variables:
        gid: a name that associates a system user with other users sharing something in common 
        name: the name of the artist
        gender: gender of the artist

    """
    
    name = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length = 1, blank=True)

    def __str__(self):
        """
        Method to create a string representing a Song Method
        Returns a string representation of the song's title field
        """

        return self.name


        class Meta:

            """
            Class defining metadata for results of querying the Album method table of music_sql_api

            """

            ordering = ('name',)

class Album(models.Model):
    """
    Class to create a table representing an Album
    Extension of models.Model

    Variables:
        gid: a name that associates a system user with other users sharing something in common 
        title: the name of the Album
        release_date: the date the album was released
        album_length: the length of the album duration

    """
    title = models.CharField(max_length=100, blank=True, default='')
    release_date = models.DateTimeField()
    album_length = models.IntegerField(default=0)
    label = models.CharField(max_length=100, blank=True, default="")
    # song = models.ManyToManyField(Song)
    # artist = models.ManyToManyField(Artist)
    

    def __str__(self):
        """
        Method to create a string representing an Album Method
        Returns a string representation of the Album's title field
        """

        return self.title

    class Meta:
        """
        Class defining metadata for results of querying the Album method table of music_sql_api
        """
        ordering = ('title',)

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
    artist = models.ForeignKey('Artist', related_name='songs', on_delete=models.CASCADE )
    genre = models.ForeignKey("Genre", related_name="songs", on_delete=models.CASCADE)
    # artist = models.ManyToManyField(Artist)
    album = models.ForeignKey('Album', related_name="songs", on_delete=models.CASCADE)
    # album = models.ManyToManyField(Album)

    def __str__(self):
        """
        Method to create a string representing a Song Method
        Returns a string representation of the song's title field
        """
        return self.title

        class Meta:

        
            ordering = ('title',)






class Genre(models.Model):
    """Class to create a table representing a genre
    extension of models.Model

    Variables:
        name: the name of the artist

    """

    name = models.CharField(max_length= 63, blank=True)

    def __str__(self):
        """
        Method to create a string representing a Genre Method
        Returns a string representation of the Genre's name
        """
        return self.name

        class Meta:

            """
            Class defining metadata for results of querying the Genre method table of music_sql_api
            """

            ordering = ('name',)

# class AlbumSong(models.Model):
#     album = models.ForeignKey('Album', related_name="album_artists", on_delete=models.CASCADE)
#     song = models.ForeignKey('Song', related_name='album_artists', on_delete=models.CASCADE)

#     def __str__(self):

#         return self.name


#         class Meta:

#             ordering = str(self.id)









