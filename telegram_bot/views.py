from telegram import Bot
import asyncio


async def send_telegram_message(message):
    bot_token = '6482291282:AAEqeVEcqcrGsr2o3eRqlhjSVAah_-8HNHo'
    chat_id = '738203440'

    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

    # TOKEN = "6482291282:AAEqeVEcqcrGsr2o3eRqlhjSVAah_-8HNHo"
    # chat_id = "738203440"
    # message = "hello from your telegram bot"
    # url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    # print(requests.get(url).json())  # this sends the message


async def main(message):
    await send_telegram_message(message)

