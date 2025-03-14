from celery import shared_task

from financial.services import CoinLoreApi


@shared_task
def fetch_global_data():
    coin_lore_api = CoinLoreApi()
    res = coin_lore_api.get_global_data()
    coin_lore_api._set_global_data(res)
    return res
