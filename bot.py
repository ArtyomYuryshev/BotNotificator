import config
import telebot
import time
from datetime import datetime

# bot token
bot = telebot.TeleBot(config.TOKEN)

# start command
@bot.message_handler(commands=["start"])
def start(message):
    HelloMessage = f"Gamarjoba, <b>{message.from_user.first_name} {message.from_user.last_name}</b>! \nЯ вам тут напоминать буду."
    bot.send_message(message.chat.id, HelloMessage, parse_mode="html")

# help command
@bot.message_handler(commands=["help"])
def get_user_text(message):
    ReminderMessage = "/start \n/help \n/reminder \n/poll"
    bot.send_message(message.chat.id, ReminderMessage, parse_mode='html')

# reminder command
@bot.message_handler(commands=["reminder"])
def get_user_text(message):
    ReminderHint = "Окай, я буду напомню вам o необходимости зарегистрироваться каждый понедельник в 11:58."
    bot.send_message(message.chat.id, ReminderHint, parse_mode="html")
    Reminder = "@snickerzzz регай!"
    while(True):
        CurrentDay = datetime.today().isoweekday()
        CurrentTime = datetime.now().strftime("%H:%M:%S")
        TimeStamp = str(CurrentDay) + "-" + CurrentTime
        print(TimeStamp)
        time.sleep(1)
        if TimeStamp == "1-11:59:00":
            print(TimeStamp)
            bot.send_message(message.chat.id, Reminder)


# poll command
@bot.message_handler(commands=["poll"])
def get_user_text(message):
    ReminderMessage = "Окай, я буду создавать опрос каждую субботу в 11:58."
    bot.send_message(message.chat.id, ReminderMessage, parse_mode="html")

# runner
bot.polling(none_stop=True)