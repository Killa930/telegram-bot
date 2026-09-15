from email.mime import image
from os import urandom

import telebot as tb
import webbrowser
from telebot import types
from urllib3.util import url
import sqlite3
import requests
import json

bot = tb.TeleBot('8691018290:AAH0uPcbx2r3YaNDKfz_RM0eXoEkDa_6mes')
API = '867b82471a6f8fab542e1bb38d9a516e'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello glad to see you!!, Text me city name: ')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data['main']['temp']
        bot.reply_to(message, f'The weather right now is {temp}')

        image = 'sunny.png' if temp > 5.0 else 'clouds.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Sorry, city not found')


bot.infinity_polling()