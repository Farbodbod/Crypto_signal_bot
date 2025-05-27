import time
import os
from telegram.ext import Updater
from telegram.error import TelegramError

TOKEN = "7887959083:AAElm33V0ojKEY1giilQs5OCDlpPd_RiZlA"
CHAT_ID = "7190856352"


def send_test_message():
    if not TOKEN or not CHAT_ID:
        print("Error: Telegram bot token or chat ID is not set.")
        return

    try:
        updater = Updater(TOKEN, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.bot.send_message(chat_id=CHAT_ID, text="سلام! ربات Railway شما در حال کار است. این یک پیام تستی است.")
        print("Test message sent successfully!")
    except TelegramError as e:
        print(f"Telegram API Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    print("Bot started. Sending test message...")
    send_test_message()
    while True:
        time.sleep(3600)
