from typing import List, Optional, TypedDict


class ICoinLoreGlobalResponse(TypedDict):
    coins_count: str
    active_markets: int
    total_mcap: int
    total_volume: int
    btc_d: float
    eth_d: float
    mcap_change: float
    volume_change: float
    avg_change_percent: float
    volume_at_24h: float
    mcap_ath: float
