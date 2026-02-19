import telebot
import os

TOKEN = os.environ.get("TOKEN")
GROUP_ID = int(os.environ.get("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_message(message):
    bot.forward_message(GROUP_ID, message.chat.id, message.message_id)

bot.polling()
