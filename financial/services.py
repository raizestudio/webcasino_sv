from abc import ABC, abstractmethod

import requests

from financial.interfaces.ICoinLore import (
    ICoinLoreGlobalResponse,
    ICoinLoreTickerResponse,
    ICoinLoreTickersResponse,
)
from financial.models import Currency, FinancialApiProvider, Ticker

# from financial.serializers import FinancialApiProviderSerializer


class AbstractApi(ABC):

    BASE_URL = None

    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    @abstractmethod
    def _set_global_data(self, data):
        """Subclasses must implement set global data."""
        ...

    @abstractmethod
    def get_global_data(self, endpoint):
        """Subclasses must implement get global data."""
        ...

    @abstractmethod
    def get_currencies(self, endpoint):
        """Subclasses must implement get currencies."""
        ...

    @abstractmethod
    def get_currency(self, endpoint, currency_id):
        """Subclasses must implement get currency."""
        ...


class CoinLoreApi(AbstractApi):

    # BASE_URL = "https://api.coinlore.net/api/"
    PAGINATION_LIMIT = 100

    def _set_global_data(self, data):
        _financial_api_provider, updated = FinancialApiProvider.objects.update_or_create(
            name="CoinLore",
            defaults={
                "coins_count": data["coins_count"],
                "active_markets_count": data["active_markets"],
                "market_cap": data["total_mcap"],
                "volume": data["total_volume"],
                "btc_dominance": data["btc_d"],
                "eth_dominance": data["eth_d"],
                "market_cap_delta": data["mcap_change"],
                "volume_delta": data["volume_change"],
                "avg_delta_percent": data["avg_change_percent"],
                "market_cap_ath": data["mcap_ath"],
            },
        )
        return _financial_api_provider

    def _set_currency_data(self, data):
        _currency, updated = Currency.objects.update_or_create(
            code=data["symbol"].lower(),
            defaults={
                "name": data["nameid"],
                "minor_unit": 8,
            },
        )

        _ticker, updated = Ticker.objects.update_or_create(
            external_id=data["id"],
            currency=_currency,
            financial_api_provider=FinancialApiProvider.objects.get(name="CoinLore"),
            defaults={
                "rank": data["rank"],
                "price_usd": data["price_usd"],
                "percent_change_24h": data["percent_change_24h"],
                "percent_change_1h": data["percent_change_1h"],
                "percent_change_7d": data["percent_change_7d"],
                "price_btc": data["price_btc"],
                "market_cap_usd": data["market_cap_usd"],
                "volume24": data["volume24"],
                "volume24a": data["volume24a"],
                "csupply": data["csupply"],
                "tsupply": data["tsupply"],
                "msupply": data["msupply"],
            },
        )
        return _ticker

    def get_global_data(self) -> ICoinLoreGlobalResponse:
        response = self.session.get(self.base_url + "global/")
        return response.json()[0]

    def get_currencies(self, start: int = 0, limit: int = 100) -> ICoinLoreTickersResponse:
        response = self.session.get(self.base_url + "tickers/")
        return response.json()

    def get_currency(self, currency_id: int) -> ICoinLoreTickerResponse:
        response = self.session.get(self.base_url + f"ticker/?id={currency_id}")
        return response.json()[0]
