import telebot
import os

TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def get_id(message):
    bot.reply_to(message, f"Chat ID: {message.chat.id}")

bot.polling()
