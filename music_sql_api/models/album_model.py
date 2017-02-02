from django.db import models
# from django.contrib.auth.models import User

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