import telebot

TOKEN = "8270067917:AAE8Zae0bt52cT3VTZDDPxJ_fuzIBHzyN1Q"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "🔥 DENAR İDDA BOT\n\nGünlük kuponlar için 👉 VIP yaz")

@bot.message_handler(func=lambda m: True)
def cevap(message):
    if "vip" in message.text.lower():
        bot.reply_to(message, "💎 VIP Üyelik\n\nÖdeme için bana yaz:\n@seninkullanici\n\nÖdeme sonrası VIP link verilecektir.")
    else:
        bot.reply_to(message, "Komutlar:\n/start\nVIP yaz")

bot.infinity_polling()
