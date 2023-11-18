# timetablereminderbot.py
# written by Khasan Rashidov
# for IUT CSE Junior Students

import telebot
import schedule
from threading import Thread
from time import sleep
from datetime import datetime

# Telegram bot token
TOKEN = '5650646500:AAEcVNDRaMQXwuGqOn71fxHyD5CJREFszKE'

bot = telebot.TeleBot(TOKEN)  # TOKEN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, " + message.from_user.first_name +
                 ". This is a timetable reminder bot for IUT junior students.")


my_chat_id = -1001508880808  # This is our (group) chat id.


def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)

# Schedule


def monday_timetable():
    timetable = '*' + "MONDAY, " + datetime.today().strftime('%d-%m-%Y') + '*' + "\n\n"
    timetable += '*' + "       ICE-20-01:" + '*' + "\n"
    timetable += '*' + "SaS" + '*' + ': 10:30 - 12:00 - A608' + "\n"
    timetable += '*' + "CA" + '*' + ': 13:30 - 15:00 - B101' + "\n"
    timetable += '*' + "Db" + '*' + ': 15:00 - 16:30 - B209' + "\n\n"
    timetable += '*' + "       CSE-20-01:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 10:30 - 12:00 - A202' + "\n"
    timetable += '*' + "ItE" + '*' + ': 12:00 - 13:30 - A203' + "\n"
    timetable += '*' + "CA" + '*' + ': 13:30 - 15:00 - B101' + "\n\n"
    timetable += '*' + "       CSE-20-02:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 09:00 - 10:30 - A202' + "\n"
    timetable += '*' + "SA" + '*' + ': 12:00 - 13:30 - B210' + "\n"
    timetable += '*' + "ItE" + '*' + ': 13:30 - 15:00 - A203' + "\n\n"
    timetable += '*' + "       CSE-20-03:" + '*' + "\n"
    timetable += 'NO CLASSES TODAY :)' + '*' + "\n\n"
    timetable += '*' + 'Your Vote Matters' + '*' + "\n"
    timetable += '*' + 'Support Jasurbek' + '*' + "\n\n"

    message = bot.send_message(my_chat_id, timetable, parse_mode='Markdown')
    return bot.pin_chat_message(chat_id=my_chat_id, message_id=message.message_id)


def tuesday_timetable():
    timetable = '*' + "TUESDAY, " + datetime.today().strftime('%d-%m-%Y') + \
        '*' + "\n\n"
    timetable += '*' + "       ICE-20-01:" + '*' + "\n"
    timetable += '*' + "ECir" + '*' + ': 09:00 - 10:30 - B201' + "\n"
    timetable += '*' + "OS" + '*' + ': 10:30 - 12:00 - A202' + "\n"
    timetable += '*' + "H2" + '*' + ': 12:00 - 13:30 - B209' + "\n"
    timetable += '*' + "Db" + '*' + ': 15:00 - 16:30 - A203' + "\n\n"
    timetable += '*' + "       CSE-20-01:" + '*' + "\n"
    timetable += '*' + "H2" + '*' + ': 10:30 - 12:00 - B101' + "\n"
    timetable += '*' + "SA" + '*' + ': 13:30 - 15:00 - B202' + "\n"
    timetable += '*' + "ItE" + '*' + ': 15:00 - 16:30 - A202' + "\n"
    timetable += '*' + "Db" + '*' + ': 16:30 - 18:00 - A202' + "\n\n"
    timetable += '*' + "       CSE-20-02:" + '*' + "\n"
    timetable += 'NO CLASSES TODAY :)' + "\n\n"
    timetable += '*' + "       CSE-20-03:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 09:00 - 10:30 - A202' + "\n"
    timetable += '*' + "SA" + '*' + ': 10:30 - 12:00 - A608' + "\n"
    timetable += '*' + "Db" + '*' + ': 13:30 - 15:00 - A203' + "\n\n"
    timetable += '*' + 'Your Vote Matters' + '*' + "\n"
    timetable += '*' + 'Support Jasurbek' + '*' + "\n\n"

    message = bot.send_message(my_chat_id, timetable, parse_mode='Markdown')
    return bot.pin_chat_message(chat_id=my_chat_id, message_id=message.message_id)


def wednesday_timetable():
    timetable = '*' + "WEDNESDAY, " + datetime.today().strftime('%d-%m-%Y') + \
        '*' + "\n\n"
    timetable += '*' + "       ICE-20-01:" + '*' + "\n"
    timetable += '*' + "ECir" + '*' + ': 09:00 - 10:30 - B201' + "\n"
    timetable += '*' + "OS" + '*' + ': 10:30 - 12:00 - A202' + "\n"
    timetable += '*' + "CA" + '*' + ': 13:30 - 15:00 - B101' + "\n"
    timetable += '*' + "SaS" + '*' + ': 15:00 - 16:30 - B101' + "\n\n"
    timetable += '*' + "       CSE-20-01:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 09:00 - 10:30 - A202' + "\n"
    timetable += '*' + "CA" + '*' + ': 13:30 - 15:00 - B101' + "\n\n"
    timetable += '*' + "       CSE-20-02:" + '*' + "\n"
    timetable += '*' + "CA" + '*' + ': 10:30 - 12:00 - B101' + "\n"
    timetable += '*' + "Db" + '*' + ': 13:30 - 15:00 - B202' + "\n"
    timetable += '*' + "ItE" + '*' + ': 15:00 - 16:30 - A203' + "\n\n"
    timetable += '*' + "       CSE-20-03:" + '*' + "\n"
    timetable += '*' + "SA" + '*' + ': 12:00 - 13:30 - B210' + "\n"
    timetable += '*' + "CA" + '*' + ': 15:00 - 16:30 - B201' + "\n"
    timetable += '*' + "ItE" + '*' + ': 16:30 - 18:00 - A202' + "\n\n"
    timetable += '*' + 'Your Vote Matters' + '*' + "\n"
    timetable += '*' + 'Support Jasurbek' + '*' + "\n\n"
    message = bot.send_message(my_chat_id, timetable, parse_mode='Markdown')
    return bot.pin_chat_message(chat_id=my_chat_id, message_id=message.message_id)


def thursday_timetable():
    timetable = '*' + "THURSDAY, " + datetime.today().strftime('%d-%m-%Y') + \
        '*' + "\n\n"
    timetable += '*' + "       ICE-20-01:" + '*' + "\n"
    timetable += 'NO CLASSES TODAY :)' + "\n\n"
    timetable += '*' + "       CSE-20-01:" + '*' + "\n"
    timetable += '*' + "SA" + '*' + ': 15:00 - 16:30 - B209' + "\n"
    timetable += '*' + "Db" + '*' + ': 16:30 - 18:00 - B201' + "\n\n"
    timetable += '*' + "       CSE-20-02:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 10:30 - 12:00 - A202' + "\n"
    timetable += '*' + "H2" + '*' + ': 12:00 - 13:30 - B201' + "\n\n"
    timetable += '*' + "       CSE-20-03:" + '*' + "\n"
    timetable += '*' + "OS" + '*' + ': 09:00 - 10:30 - A202' + "\n"
    timetable += '*' + "H2" + '*' + ': 10:30 - 12:00 - B209' + "\n\n"
    timetable += '*' + 'Your Vote Matters' + '*' + "\n"
    timetable += '*' + 'Support Jasurbek' + '*' + "\n\n"

    message = bot.send_message(my_chat_id, timetable, parse_mode='Markdown')
    return bot.pin_chat_message(chat_id=my_chat_id, message_id=message.message_id)


def friday_timetable():
    timetable = '*' + "FRIDAY, " + datetime.today().strftime('%d-%m-%Y') + '*' + "\n\n"
    timetable += '*' + "       ICE-20-01:" + '*' + "\n"
    timetable += 'NO CLASSES TODAY :)' + "\n\n"
    timetable += '*' + "       CSE-20-01:" + '*' + "\n"
    timetable += 'NO CLASSES TODAY :)' + "\n\n"
    timetable += '*' + "       CSE-20-02:" + '*' + "\n"
    timetable += '*' + "CA" + '*' + ': 13:30 - 15:00 - B101' + "\n"
    timetable += '*' + "Db" + '*' + ': 15:00 - 16:30 - A203' + "\n"
    timetable += '*' + "SA" + '*' + ': 16:30 - 18:00 - B201' + "\n\n"
    timetable += '*' + "       CSE-20-03:" + '*' + "\n"
    timetable += '*' + "CA" + '*' + ': 10:30 - 12:00 - B101' + "\n"
    timetable += '*' + "ItE" + '*' + ': 12:00 - 13:30 - A203' + "\n"
    timetable += '*' + "Db" + '*' + ': 13:30 - 15:00 - A203' + "\n\n"
    timetable += '*' + 'Your Vote Matters' + '*' + "\n"
    timetable += '*' + 'Support Jasurbek' + '*' + "\n\n"

    message = bot.send_message(my_chat_id, timetable, parse_mode='Markdown')
    return bot.pin_chat_message(chat_id=my_chat_id, message_id=message.message_id)


if __name__ == '__main__':
    # Create the job in schedule.
    schedule.every().monday.at("07:30").do(monday_timetable)
    schedule.every().tuesday.at("07:30").do(tuesday_timetable)
    schedule.every().wednesday.at("07:30").do(wednesday_timetable)
    schedule.every().thursday.at("07:30").do(thursday_timetable)
    schedule.every().friday.at("07:30").do(friday_timetable)

    # Spin up a thread to run the schedule check so it doesn't block your bot.
    # This will take the function schedule_checker which will check every second
    # to see if the scheduled job needs to be ran.
    Thread(target=schedule_checker).start()

bot.polling(none_stop=True)
