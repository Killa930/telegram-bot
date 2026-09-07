import telebot as tb
import webbrowser

bot = tb.TeleBot('8691018290:AAH0uPcbx2r3YaNDKfz_RM0eXoEkDa_6mes')


@bot.message_handler(commands=['site', 'website', 'youtube'])
def site(message):
    webbrowser.open_new_tab('www.youtube.com')



@bot.message_handler(commands=['start', 'main', "hello"])
def main(message):
    bot.send_message(message.chat.id, f"Hello!!! {message.from_user.first_name} {message.from_user.last_name}")

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "<b>Help</b> <em><u>information</u></em>", parse_mode='HTML')

@bot.message_handler(commands=['myUsername'])
def main(message):
    bot.send_message(message.chat.id, message.from_user.username, parse_mode='HTML')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f"Hello!!! {message.from_user.first_name} {message.from_user.last_name}")
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.infinity_polling()