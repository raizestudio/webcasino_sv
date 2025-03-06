from django.db import models


class Currency(models.Model):
    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    minor_unit = models.IntegerField()
    symbol = models.CharField(max_length=10)
    is_crypto = models.BooleanField(default=False)
    can_deposit = models.BooleanField(default=False)
    can_withdraw = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    balance = models.FloatField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, to_field="code")

    def __str__(self):
        return f"{self.user.username}'s wallet"


class Pool(models.Model):
    balance = models.FloatField()

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
