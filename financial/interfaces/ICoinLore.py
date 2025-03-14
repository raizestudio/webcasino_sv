from typing import List, TypedDict


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


class ICoinLoreTickerResponse(TypedDict):
    id: str
    symbol: str
    name: str
    nameid: str
    rank: int
    price_usd: str
    percent_change_24h: str
    percent_change_1h: str
    percent_change_7d: str
    price_btc: str
    market_cap_usd: str
    volume24: str
    volume24a: str
    csupply: str
    tsupply: str
    msupply: str


class ICoinLoreTickersResponse(TypedDict):
    data: List[ICoinLoreTickerResponse]
    info: dict[
        "coins_num":int,
        "time":int,
    ]
