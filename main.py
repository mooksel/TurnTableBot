import telebot

token = "513777236:AAGznaDind0_iIelgAnguG6cgJ3_22E71ZY"
bot = telebot.TeleBot(token)

'''
	shrug - Shrugs.
	turn_table - Turns table.
	take_my_energy - Gives you energy.
	lenny - Lenny.
	chlen - Visits your mama.
	disapproval - Make me unsee it!
	'''

@bot.message_handler(commands=['shrug'])
def handle_shrug(message):
	bot.send_message(message.chat.id, "¯\_(ツ)_/¯")


@bot.message_handler(commands=['turn_table'])
def handle_turn_table(message):
	bot.send_message(message.chat.id, "(╯°□°）╯︵ ┻━┻")

@bot.message_handler(commands=['take_my_energy'])
def handle_turn_table(message):
	bot.send_message(message.chat.id, "༼ つ ◕_◕ ༽つ")

@bot.message_handler(commands=['lenny'])
def handle_turn_table(message):
	bot.send_message(message.chat.id, "( ͡° ͜ʖ ͡°)")

@bot.message_handler(commands=['chlen'])
def handle_turn_table(message):
	bot.send_message(message.chat.id, "8========3")

@bot.message_handler(commands=['disapproval'])
def handle_turn_table(message):
	bot.send_message(message.chat.id, "ಠ_ಠ")


@bot.message_handler(content_types=['text'])
def handle_text(message):
	if "три сотни" in message.text:
		bot.send_message(message.chat.id, "Отсоси у программиста")
	if message.text.endswith("300") or message.text.endswith("триста"):
		bot.send_message(message.chat.id, "Отсоси у программиста")
	if message.text.endswith("влад") or message.text.endswith("Влад"):
		bot.send_message(message.chat.id, "ебал томат")
	if message.text.endswith("дима") or message.text.endswith("Дима") or message.text.endswith("Димасик") or message.text.endswith("димасик"):
		bot.send_message(message.chat.id, "пьет пивасик")
	if message.text.endswith("алексей") or message.text.endswith("Алексей"):
		bot.send_message(message.chat.id, "ебал гусей")
	if message.text.endswith("мразота") or message.text == "иди нахуй":
		bot.send_message(message.chat.id, "Проверяй за щекой")
	if message.text.endswith("пидор"):
		bot.send_message(message.chat.id, "Сам пидор")
	if message.text.endswith("леха") or message.text.endswith("Леха"):
		bot.send_message(message.chat.id, "Лепеха")
	if "бля" in message.text or "сука" in message.text:
		bot.send_message(message.chat.id, "И этими губами ты целуешь свою маму?")


bot.polling(none_stop=True, interval=0)
