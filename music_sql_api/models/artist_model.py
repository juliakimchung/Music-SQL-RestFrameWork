from django.db import models



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
