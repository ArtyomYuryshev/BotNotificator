import config
import telebot
import time
from datetime import datetime

# bot token
bot = telebot.TeleBot(config.TOKEN)

# help command
@bot.message_handler(commands=["help"])
def get_user_text(message):
    ReminderMessage = "/help \n/reminder \n/poll"
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
        TimeStamp1 = str(CurrentDay) + "-" + CurrentTime
        time.sleep(1)
        if TimeStamp1 == "2-21:41:00":
            print(TimeStamp1)
            bot.send_message(message.chat.id, Reminder)

# poll command
@bot.message_handler(commands=["poll"])
def get_user_text(message):
    ReminderMessage = "Окай, я буду создавать опрос каждую субботу в 11:58."
    bot.send_message(message.chat.id, ReminderMessage, parse_mode="html")
    while(True):
        CurrentDay = datetime.today().isoweekday()
        CurrentTime = datetime.now().strftime("%H:%M:%S")
        TimeStamp2 = str(CurrentDay) + "-" + CurrentTime
        time.sleep(1)
        if TimeStamp2 == "2-21:41:00":
            CurrentWednsday = datetime.now().strftime("%d:%m")
            PollHeader = "mzgb - "+ CurrentWednsday
            print(PollHeader)
            bot.send_poll(message.chat.id, PollHeader, ["Иду", "Не иду"], False, "regular", False)

# runner
bot.polling(none_stop=True)