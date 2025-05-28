# signal_generator.py

from mexc_api import fetch_ohlcv
from utils.indicators import calculate_indicators
import pandas as pd

def generate_signal(symbol: str, timeframe: str) -> dict:
    """
    Generate trading signal for a given symbol and timeframe.
    Returns a dict with signal details.
    """
    data = fetch_ohlcv(symbol, timeframe, limit=100)
    df = pd.DataFrame(data, columns=["timestamp", "open", "high", "low", "close", "volume"])
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
    df.set_index("timestamp", inplace=True)

    df = calculate_indicators(df)
    last = df.iloc[-1]

    if last["EMA20"] > last["EMA50"] and last["RSI"] < 70 and last["MACD"] > last["MACD_signal"]:
        signal = "LONG"
    elif last["EMA20"] < last["EMA50"] and last["RSI"] > 30 and last["MACD"] < last["MACD_signal"]:
        signal = "SHORT"
    else:
        signal = "NEUTRAL"

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "signal": signal,
        "price": last["close"],
        "rsi": round(last["RSI"], 2)
    }
