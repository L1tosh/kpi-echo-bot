import telebot
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path='../conf/config.env')


TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello! I'm echo bot!")

@bot.message_handler(func=lambda message: True)
def send_message_without_reply(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True, interval=0)