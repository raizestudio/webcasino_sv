from django.db import models

from core.models import ApiProvider


class Currency(models.Model):
    """The currency model"""

    code = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    minor_unit = models.IntegerField(default=2)
    symbol = models.CharField(max_length=10)
    # is_crypto = models.BooleanField(default=False)
    can_deposit = models.BooleanField(default=False)
    can_withdraw = models.BooleanField(default=False)
    is_free = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "currencies"

    def __str__(self):
        return self.name


class Ticker(models.Model):
    """The ticker model"""

    external_id = models.CharField(max_length=100)
    rank = models.IntegerField()
    price_usd = models.FloatField()
    percent_change_24h = models.FloatField()
    percent_change_1h = models.FloatField()
    percent_change_7d = models.FloatField()
    price_btc = models.FloatField()
    market_cap_usd = models.FloatField()
    volume24 = models.FloatField()
    volume24a = models.FloatField()
    csupply = models.FloatField()
    tsupply = models.FloatField()
    msupply = models.FloatField()

    currency = models.ForeignKey("Currency", on_delete=models.CASCADE)
    exchange = models.ForeignKey("Exchange", on_delete=models.CASCADE, null=True)
    financial_api_provider = models.ForeignKey("FinancialApiProvider", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("currency", "exchange")

    def __str__(self):
        return f"{self.currency.code} on {self.exchange.name}"


class Exchange(models.Model):
    """The exchange model"""

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
    """The wallet model"""

    balance = models.FloatField()

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, to_field="code")

    def __str__(self):
        return f"{self.user.username}'s wallet"


class Pool(models.Model):
    """The pool model"""

    balance = models.FloatField()

    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
