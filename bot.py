import telebot
from telebot import types

import configs.config as config
import owm

bot = telebot.TeleBot(token=config.token)


@bot.message_handler(regexp='t')
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Forecast')
    itembtn2 = types.KeyboardButton('weather now')
    itembtn3 = types.KeyboardButton('plot')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, message.text, reply_markup=markup)

    process_select_step(message)


def process_select_step(message):
    try:
        if message.text == 'weather now':
            bot.send_message(message.chat.id, owm.get_owm(), parse_mode='Markdown')
        elif message.text == 'Forecast':
            bot.send_message(message.chat.id, owm.get_owm(), parse_mode='Markdown')
        #elif message.text == 'plot':
            # plot.get_plot()
            #bot.send_photo(message.chat.id, open('/home/opc/plot.png', 'rb'))
    except Exception as e:
        bot.reply_to(message, '{}'.format(e))

if __name__ == '__main__':
    bot.polling(none_stop=True)