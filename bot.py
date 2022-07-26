import config
import telebot
import time
from datetime import datetime

# bot token
bot = telebot.TeleBot(config.TOKEN)

"""
It sends a list of available commands
"""
@bot.message_handler(commands=["help"])
def get_user_text(message):
    ReminderMessage = "/help \n/reminder \n/poll"
    bot.send_message(message.chat.id, ReminderMessage, parse_mode='html')

"""
It sends reply to the user, then it checks if the current day is Monday and the current time is
11:59:00. If it is, it sends a message
"""
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
        if TimeStamp1 == "1-11:59:00":
            print(TimeStamp1)
            bot.send_message(message.chat.id, Reminder)


"""
It sends reply to the user, then it checks if the current day is Saturday and the current time is
11:59:00. If it is, it sends a poll
"""
@bot.message_handler(commands=["poll"])
def get_user_text(message):
    ReminderMessage = "Окай, я буду создавать опрос каждую субботу в 11:58."
    bot.send_message(message.chat.id, ReminderMessage, parse_mode="html")
    while(True):
        CurrentDay = datetime.today().isoweekday()
        CurrentTime = datetime.now().strftime("%H:%M:%S")
        TimeStamp2 = str(CurrentDay) + "-" + CurrentTime
        time.sleep(1)
        if TimeStamp2 == "6-11:59:00":
            CurrentWednsday = datetime.now().strftime("%d:%m")
            PollHeader = "mzgb - "+ CurrentWednsday
            print(PollHeader)
            bot.send_poll(message.chat.id, PollHeader, ["Иду", "Не иду"], False, "regular", False)

# runner
bot.polling(none_stop=True)