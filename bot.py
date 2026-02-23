import telebot
import os

TOKEN = os.getenv("TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

# User yozsa → guruhga yuboradi (ID bilan)
@bot.message_handler(func=lambda message: message.chat.type == "private")
def forward_to_group(message):
    text = f"User ID: {message.chat.id}\n\n{message.text}"
    bot.send_message(GROUP_ID, text)

# Guruhda reply qilinsa → userga qaytaradi
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID and message.reply_to_message)
def reply_to_user(message):
    original_text = message.reply_to_message.text
    
    if "User ID:" in original_text:
        user_id = int(original_text.split("\n")[0].replace("User ID: ", ""))
        bot.send_message(user_id, message.text)

bot.infinity_polling()
