from django.db import models

from core.models import ApiProvider


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


class Exchange(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "exchanges"

    def __str__(self):
        return self.name


class FinancialApiProvider(ApiProvider):
    """The financial API provider model"""

    coins_count = models.IntegerField(default=0)
    active_markets_count = models.IntegerField(default=0)
    market_cap = models.FloatField(default=0)
    volume = models.FloatField(default=0)
    btc_dominance = models.FloatField(default=0)
    eth_dominance = models.FloatField(default=0)
    market_cap_delta = models.FloatField(default=0)
    volume_delta = models.FloatField(default=0)
    avg_delta_percent = models.FloatField(default=0)
    # volume_24h = models.FloatField(default=0)
    market_cap_ath = models.FloatField(default=0)  # All time high

    class Meta:
        verbose_name = "Financial API Provider"
        verbose_name_plural = "Financial API Providers"


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
