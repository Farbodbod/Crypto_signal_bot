# telegram_bot.py

from telegram import Bot
from config import BOT_TOKEN, TELEGRAM_USER_ID

bot = Bot(token=BOT_TOKEN)

def send_signal_message(signal_data: dict):
    """
    Send a formatted signal message to the configured Telegram user.
    """
    message = (
        f"📊 Signal for {signal_data['symbol']} ({signal_data['timeframe']})\n"
        f"🟢 Type: {signal_data['signal']}\n"
        f"💰 Price: {signal_data['price']}\n"
        f"📈 RSI: {signal_data['rsi']}\n"
    )
    bot.send_message(chat_id=TELEGRAM_USER_ID, text=message)
