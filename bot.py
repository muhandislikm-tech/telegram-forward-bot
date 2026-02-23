import telebot
import os

TOKEN = os.getenv("TOKEN")
GROUP_ID = int(os.getenv("GROUP_ID"))

bot = telebot.TeleBot(TOKEN)

# 1️⃣ User yozsa → guruhga ism + username + ID bilan yuboradi
@bot.message_handler(func=lambda message: message.chat.type == "private")
def forward_to_group(message):
    name = message.from_user.first_name or ""
    username = f"@{message.from_user.username}" if message.from_user.username else "username yo‘q"
    user_id = message.chat.id

    text = (
        f"👤 Ism: {name}\n"
        f"🔗 Username: {username}\n"
        f"🆔 User ID: {user_id}\n\n"
        f"💬 Xabar:\n{message.text}"
    )

    bot.send_message(GROUP_ID, text)

# 2️⃣ Guruhda reply qilinsa → userga qaytaradi
@bot.message_handler(func=lambda message: message.chat.id == GROUP_ID and message.reply_to_message)
def reply_to_user(message):
    original_text = message.reply_to_message.text

    if "User ID:" in original_text:
        user_id_line = [line for line in original_text.split("\n") if "User ID:" in line][0]
        user_id = int(user_id_line.replace("🆔 User ID: ", ""))
        bot.send_message(user_id, message.text)

bot.infinity_polling()
