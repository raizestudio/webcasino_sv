from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    rating = models.FloatField()

    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
