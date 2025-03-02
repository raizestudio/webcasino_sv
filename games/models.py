from django.db import models
from polymorphic.models import PolymorphicModel


class GameCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(PolymorphicModel):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(null=True)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
