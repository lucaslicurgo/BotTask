import telebot 
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'), parse_mode='HTML')

@bot.message_handler(commands=['start', 'Start', 'START'])
def start_message(message):
    bot.send_message(message.chat.id, 'Teste')

bot.infinity_polling()