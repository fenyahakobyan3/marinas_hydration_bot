import telebot
import schedule
import time
from threading import Thread

# Replace 'YOUR_API_TOKEN' with the token you received from BotFather
API_TOKEN = '7305513452:AAGHsRxJ3NO6o-eNjHbpBf2Q7pp30LbxMm8'
CHAT_ID = '1114198707'  # Replace with your girlfriend's chat ID

bot = telebot.TeleBot(API_TOKEN)

# List of loving messages
messages = [
    "Don't forget to drink water, my love! 💧❤️",
    "Stay hydrated, beautiful! 🌸💧",
    "Time for a water break, sweetheart! 💦😘",
    "Remember to drink water, my dear! 🥰💧",
    "Hydration is key, darling! 💧💖"
]

def send_water_reminder():
    bot.send_message(CHAT_ID, "Time to drink some water! 💧")
    bot.send_message(CHAT_ID, random.choice(messages))

# Schedule the reminder every 2 hours
schedule.every(2).hours.do(send_water_reminder)

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduler in a new thread
thread = Thread(target=run_scheduler)
thread.start()

# Start the bot
bot.polling()
