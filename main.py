import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['Merhaba'])
def merhaba(message):
  bot.reply_to(message, "Merhaba Hoş Geldiniz")

  bot.polling()
