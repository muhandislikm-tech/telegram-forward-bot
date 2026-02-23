import telebot
import os

TOKEN = os.getenv("TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

# 1) User yozsa → guruhga forward
@bot.message_handler(func=lambda message: message.chat.type == "private")
def forward_to_group(message):
    bot.forward_message(
        GROUP_ID,
        message.chat.id,
        message.message_id
    )

# 2) Guruhda reply qilinsa → userga qaytar
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID and message.reply_to_message)
def reply_to_user(message):
    original = message.reply_to_message

    # Forward qilingan xabarda forward_from bo‘ladi
    if original.forward_from:
        user_id = original.forward_from.id
        bot.send_message(user_id, message.text)

bot.infinity_polling()
