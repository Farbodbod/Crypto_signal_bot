# main.py

import time
import schedule
from config import SYMBOLS, TIMEFRAMES
from signal_generator import generate_signal
from telegram_bot import send_signal_message

def run_analysis():
    for symbol in SYMBOLS:
        for timeframe in TIMEFRAMES:
            try:
                result = generate_signal(symbol, timeframe)
                if result["signal"] in ["LONG", "SHORT"]:
                    send_signal_message(result)
            except Exception as e:
                print(f"Error processing {symbol} {timeframe}: {e}")

if __name__ == "__main__":
    # Schedule analysis every 15 minutes
    schedule.every(15).minutes.do(run_analysis)
    print("Crypto Signal Bot is running...")
    while True:
        schedule.run_pending()
        time.sleep(1)
