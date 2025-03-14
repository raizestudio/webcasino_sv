from abc import ABC, abstractmethod

import requests

from financial.interfaces.ICoinLore import ICoinLoreGlobalResponse
from financial.models import FinancialApiProvider
from financial.serializers import FinancialApiProviderSerializer


class AbstractApi(ABC):

    BASE_URL = None

    def __init__(self):
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

    BASE_URL = "https://api.coinlore.net/api/"

    def __init__(self):
        self.session = requests.Session()

    def _set_global_data(self, data):
        _financial_api_provider, updated = FinancialApiProvider.objects.update_or_create(
            name="Coin Lore",
            coins_count=data["coins_count"],
            active_markets_count=data["active_markets"],
            market_cap=data["total_mcap"],
            volume=data["total_volume"],
            btc_dominance=data["btc_d"],
            eth_dominance=data["eth_d"],
            market_cap_delta=data["mcap_change"],
            volume_delta=data["volume_change"],
            avg_delta_percent=data["avg_change_percent"],
            market_cap_ath=data["mcap_ath"],
        )
        return _financial_api_provider

    def get_global_data(self) -> ICoinLoreGlobalResponse:
        response = self.session.get(self.BASE_URL + "global/")
        return response.json()[0]

    def get_currencies(self):
        response = self.session.get(self.BASE_URL + "tickers/")
        return response.json()

    def get_currency(self, currency_id):
        response = self.session.get(self.BASE_URL + f"ticker/?id={currency_id}")
        return response.json()
