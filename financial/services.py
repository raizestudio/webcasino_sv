import requests


class CoinLoreApi:

    BASE_URL = "https://api.coinlore.net/api/"

    def __init__(self):
        self.session = requests.Session()

    def get_global_data(self):
        response = self.session.get(self.BASE_URL + "global/")
        return response.json()
