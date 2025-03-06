from django.db import models


class GameCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(null=True)
    rating = models.FloatField(default=0)
    preview_image = models.ImageField(upload_to="games", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Slot(models.Model):
    reels = models.IntegerField(default=3)
    rows = models.IntegerField(default=3)
    paylines = models.IntegerField(default=1)
    min_bet = models.FloatField(default=0)
    max_bet = models.FloatField(default=0)
    buy_feature = models.BooleanField(default=False)
    bonus_game = models.BooleanField(default=False)
    free_spins = models.BooleanField(default=False)
    jackpot = models.BooleanField(default=False)

    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="slots")

    def __str__(self):
        return self.name
