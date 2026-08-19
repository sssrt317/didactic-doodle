import telebot

# التوكن الشغال والخاص ببوتك الحالي
BOT_TOKEN = "8913110854:AAEQvVsEjztYowdL6A4W87b_d9Gm-dfggM8"
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🛡️ أهلاً بكم! أنا بوت حماية المجموعات المطور.")

@bot.message_handler(func=lambda message: "http" in message.text.lower() or "t.me" in message.text.lower())
def delete_links(message):
    status = bot.get_chat_member(message.chat.id, message.from_user.id).status
    if status not in ['creator', 'administrator']:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "⚠️ الروابط ممنوعة هنا!")

@bot.message_handler(func=lambda message: message.text == "حظر" and message.reply_to_message)
def ban_user(message):
    status = bot.get_chat_member(message.chat.id, message.from_user.id).status
    if status in ['creator', 'administrator']:
        user_id = message.reply_to_message.from_user.id
        bot.ban_chat_member(message.chat.id, user_id)
        bot.reply_to(message, "🚫 تم حظر العضو بنجاح.")

bot.infinity_polling()
