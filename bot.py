import time
import telebot, types
import config
from flask import Flask, request
import os

bot = telebot.TeleBot(config.token)

server = Flask(__name__)

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

@bot.message_handler(func=lambda message: True, content_types=["text"])
def default_test(message):
    keyboard = types.ReplyKeyboardMarkup()
    url_button = types.KeyboardButton(text="Перейти на Яндекс")
    keyboard.add(url_button)

server.run(host="0.0.0.0", port=os.environ.get('PORT', 5000))

 #   bot.set_webhook(url="https://chatbot0939.herokuapp.com/"+config.token)
#if __name__ == '__main__':
   # bot.polling(none_stop=True)