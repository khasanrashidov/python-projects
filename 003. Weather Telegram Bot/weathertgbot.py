 # weathertgbot.py was written by Khasan Rashidov

import telebot
import pyowm

bot = telebot.TeleBot("5432102554:AAGntY61pLlmdjx9XNF3beUwgaNlNFfUvQI") # TOKEN

owm = pyowm.OWM('6d00d1d4e704068d70191bad2673e0cc') # API KEY
mgr = owm.weather_manager()

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, " + message.from_user.first_name + ". Please enter the name of the city or country to get its weather info.")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    try:
        observation = mgr.weather_at_place(message.text)
        w = observation.weather

        weather_info = '*' + message.text + '*' + " weather information:" + "\n"
        weather_info += "\n"
        weather_info += '*' + "Weather status:   " + '*' + str(w.detailed_status) + "\n"
        weather_info += '*' + "Wind speed:   " + '*' + str(w.wind()['speed']) + " m/s" + "\n"
        weather_info += '*' + "Humidity:   " + '*' + str(w.humidity) + " %" + "\n"
        weather_info += '*' + "Temperature:   " + '*' + str(w.temperature('celsius')['temp']) + " °C" + "\n"
        weather_info += '*' + "Feels like:   " + '*' + str(w.temperature('celsius')['feels_like']) + " °C" + "\n"
        weather_info += '*' + "Clouds:   " + '*' + str(w.clouds) + " %" + "\n"

        bot.send_message(message.chat.id, weather_info, parse_mode='Markdown')
    except pyowm.commons.exceptions.NotFoundError:
        weather_info = 'Wrong city or country name, please try again with different name!' + '\n'
        
        bot.send_message(message.chat.id, weather_info, parse_mode='Markdown')

bot.polling(none_stop = True)
