from os import urandom

import telebot as tb
import webbrowser
from telebot import types
from urllib3.util import url

bot = tb.TeleBot('8691018290:AAH0uPcbx2r3YaNDKfz_RM0eXoEkDa_6mes')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('On site')
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Change text')
    markup.row(btn1)
    markup.row(btn2, btn3)
    file = open('photo.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hello', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'On site':
        bot.send_message(message.chat.id, 'website is open')
    elif message.text == 'Delete photo':
        bot.send_message(message.chat.id, 'delete')
    elif message.text == 'Change text':
        bot.send_message(message.chat.id, 'change text')

@bot.message_handler(content_types=['photo', 'sticker'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Perejti na sajt', url='https://google.com')
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Change text', callback_data='edit')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.reply_to(message, 'What a beautiful photo!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text:', callback.message.chat.id, callback.message.message_id)




bot.infinity_polling()