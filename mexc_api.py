# mexc_api.py

import ccxt
from config import MEXC_API_KEY, MEXC_SECRET_KEY

def get_mexc_client():
    """Initialize and return an authenticated MEXC client."""
    return ccxt.mexc({
        'apiKey': MEXC_API_KEY,
        'secret': MEXC_SECRET_KEY,
        'enableRateLimit': True
    })

def fetch_ohlcv(symbol: str, timeframe: str = "15m", limit: int = 100):
    """
    Fetch OHLCV data for a given symbol and timeframe.
    Returns a list of [timestamp, open, high, low, close, volume].
    """
    client = get_mexc_client()
    return client.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
