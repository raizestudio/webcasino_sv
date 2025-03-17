import logging

from celery import group, shared_task

from financial.models import FinancialApiProvider
from financial.services import CoinLoreApi

API_PROVIDERS_MAP = {
    "CoinLore": CoinLoreApi,
}


@shared_task
def fetch_provider_data(provider_name):
    """Fetch data for a single API provider."""
    api_provider_cls = API_PROVIDERS_MAP.get(provider_name)

    if not api_provider_cls:
        return {"status": "error", "provider": provider_name, "reason": "Unknown provider"}

    try:
        api_base_url = FinancialApiProvider.objects.get(name=provider_name).base_url
        api_provider = api_provider_cls(api_base_url)
        res = api_provider.get_global_data()
        api_provider._set_global_data(res)

        coins_count = res["coins_count"]
        pages_count = (coins_count - 99) // 100

        # for page in range(1, pages_count):
        for page in range(0, 1):
            res_currencies = api_provider.get_currencies()
            print(f"Res currencies: {res_currencies}")
            for currency in res_currencies["data"]:
                cleaned_currency = {key: (None if currency.get(key, None) in ["''.", "", None] else currency.get(key)) for key in currency}
                print(currency)
                api_provider._set_currency_data(cleaned_currency)

        # res_ticker = api_provider.get_currency(90)
        # print(res_ticker)
        # api_provider._set_currency_data(res_ticker)
        return {"status": "success", "provider": provider_name}

    except Exception as e:
        return {"status": "error", "provider": provider_name, "reason": str(e)}


@shared_task
def fetch_api_data():
    """Creates and runs a group of tasks in parallel for all API providers."""
    provider_names = FinancialApiProvider.objects.values_list("name", flat=True)

    if not provider_names:
        return {"status": "error", "reason": "No providers available"}

    # Create a group of fetch_provider_data tasks
    task_group = group(fetch_provider_data.s(provider_name) for provider_name in provider_names)

    # Execute tasks in parallel
    results = task_group.apply_async()

    return {"status": "submitted", "task_group_id": results.id}
