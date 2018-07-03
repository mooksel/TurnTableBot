import telebot

token = "513777236:AAGznaDind0_iIelgAnguG6cgJ3_22E71ZY"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['shrug'])
def handle_shrug(message):
    bot.send_message(message.chat.id, "¯\_(ツ)_/¯")


@bot.message_handler(commands=['turn_table'])
def handle_turn_table(message):
    bot.send_message(message.chat.id, "(╯°□°）╯︵ ┻━┻")


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.endswith("пидор"):
        bot.send_message(message.chat.id, "Сам пидор")
    elif "бля" in message.text or "сука" in message.text:
        bot.send_message(message.chat.id, "И этими губами ты целуешь свою маму?")


bot.polling(none_stop=True, interval=0)
