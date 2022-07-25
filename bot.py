import telebot

bot = telebot.TeleBot("")

# start action
@bot.message_handler(commands=["start"])
def start(message):
    HelloMessage = f"Gamarjoba, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! \nЯ вам тут напоминать буду."
    bot.send_message(message.chat.id, HelloMessage, parse_mode="html")

# help command
@bot.message_handler(commands=["help"])
def get_user_text(message):
    ReminderMessage = "/start \n/help \n/reminder \n/poll"
    bot.send_message(message.chat.id, ReminderMessage, parse_mode='html')

# other action
@bot.message_handler(commands=["reminder"])
def get_user_text(message):
    ReminderMessage = "Окай, я буду напомню вам о необходимости зарегистрироваться каждый понедельник в 11:58."
    bot.send_message(message.chat.id, ReminderMessage, parse_mode="html")

# other action
@bot.message_handler(commands=["poll"])
def get_user_text(message):
    ReminderMessage = "Окай, я буду создавать опрос каждую субботу в 11:58."
    bot.send_message(message.chat.id, ReminderMessage, parse_mode="html")

# runner
bot.polling(none_stop=True)