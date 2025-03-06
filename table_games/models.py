import random
import uuid

from django.db import models

from games.models import Game


class Deck(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "decks"

    def __str__(self):
        return str(self.id)

    @staticmethod
    def generate_deck(seed: str = None) -> list[str]:
        """
        Generates a unique but consistent deck order based on the given UUID string.
        If no seed is provided, a random deck is generated.
        """
        RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        SUITS = ["s", "h", "d", "c"]
        deck = [rank + suit for rank in RANKS for suit in SUITS]

        if seed:
            seed_int = int(uuid.UUID(seed))
            rng = random.Random(seed_int)
            rng.shuffle(deck)

        return deck


class Table(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    decks = models.ManyToManyField(Deck, related_name="tables")

    class Meta:
        # abstract = True
        verbose_name_plural = "tables"


class Poker(Game):
    # flop_cards = models.IntegerField()
    # turn_cards = models.IntegerField()
    # river_cards = models.IntegerField()
    # small_blind = models.IntegerField()
    # big_blind = models.IntegerField()
    # ante = models.IntegerField()
    # max_players = models.IntegerField()
    # min_players = models.IntegerField()
    # max_rounds = models.IntegerField()
    # max_raise = models.IntegerField()
    # max_bet = models.IntegerField()
    # max_call = models.IntegerField()
    # max_check = models.IntegerField()
    # max_fold = models.IntegerField()
    # max_all_in = models.IntegerField()
    # max_showdown = models.IntegerField()
    timeout = models.IntegerField()


class TexasHoldEm(Poker):

    deck_cards = models.IntegerField()
