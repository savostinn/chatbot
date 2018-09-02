import time
import telebot
from telebot import types
import config
from flask import Flask, request
import os

bot = telebot.TeleBot(config.token)

server = Flask(__name__)
a=["Привет, смертный","Как дела, человечишка","Чем занимаешься", "Круто, хорошего дня"]
b=["Привет, бот", "Хорошо", "Пишу код для тебя", "Пока"]
i=0
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

#@bot.message_handler(func=lambda message: True, content_types=['text'])
#def echo_message(message):
#    bot.reply_to(message, message.text)


@server.route('/'+config.token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://chatbot0939.herokuapp.com/"+config.token)
    return "!", 200

@bot.message_handler(content_types=['text'])
def dialog(message):
    # Эти параметры для клавиатуры необязательны, просто для удобства
    global a
    global b
    global i
    if(i<=len(a)):
	    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
	    button_phone = types.KeyboardButton(text=a[i])
	    keyboard.add(button_phone)
	    bot.send_message(message.chat.id, b[i], reply_markup=keyboard)
	    i+=1


server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

 #   bot.set_webhook(url="https://chatbot0939.herokuapp.com/"+config.token)
#if __name__ == '__main__':
   # bot.polling(none_stop=True)