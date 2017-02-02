from django.db import models

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