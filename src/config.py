from dataclasses import dataclass

@dataclass
class DataConfig:
    raw_price_path: str = "data/raw/BrentOilPrices.csv"
    event_path: str = "data/events/oil_market_events.csv"

@dataclass
class ModelConfig:
    draws: int = 2000
    tune: int = 1000
    chains: int = 2
