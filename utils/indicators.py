# utils/indicators.py

import pandas as pd
import ta

def calculate_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate technical indicators and append them to the DataFrame.
    Indicators: EMA20, EMA50, RSI, MACD, MACD Signal, Bollinger Bands.
    """
    df["EMA20"] = ta.trend.EMAIndicator(df["close"], window=20).ema_indicator()
    df["EMA50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    df["RSI"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    macd = ta.trend.MACD(df["close"])
    df["MACD"] = macd.macd()
    df["MACD_signal"] = macd.macd_signal()
    bb = ta.volatility.BollingerBands(df["close"], window=20, window_dev=2)
    df["BOLL_HIGH"] = bb.bollinger_hband()
    df["BOLL_MID"] = bb.bollinger_mavg()
    df["BOLL_LOW"] = bb.bollinger_lband()
    return df
