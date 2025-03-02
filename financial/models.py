from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.FloatField()  # in USD
    is_crypto = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    balance = models.FloatField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wallet"
