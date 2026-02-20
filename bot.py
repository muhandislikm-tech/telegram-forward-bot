import telebot
import os

TOKEN = os.getenv("TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def forward_to_group(message):
    bot.forward_message(
        GROUP_ID,
        message.chat.id,
        message.message_id
    )

bot.infinity_polling()
