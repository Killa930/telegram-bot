from os import urandom

import telebot as tb
import webbrowser
from telebot import types
from urllib3.util import url
import sqlite3

bot = tb.TeleBot('8691018290:AAH0uPcbx2r3YaNDKfz_RM0eXoEkDa_6mes')
name = None



@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id)
    conn = sqlite3.connect('DB.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, "Привет, сейчас тебя зарегаем братк!")
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('DB.sql')
    cur = conn.cursor()

    cur.execute(f'INSERT INTO users (name, pass) VALUES ("{name}", "{password}")')
    conn.commit()
    cur.close()
    conn.close()

    markup = tb.types.InlineKeyboardMarkup()
    markup.add(tb.types.InlineKeyboardButton('Список пз', callback_data='users'))
    bot.send_message(message.chat.id, 'Uspeshno!!!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('DB.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''
    for el in users:
        info += f'Name: {el[1]}, password: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)


bot.infinity_polling()