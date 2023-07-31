import os

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Avenir! Would you like to buy or sell crypto? Type /BUY for buy, /SELL for sell, or /SUBSCRIBE to view our trader subscription options.")


@bot.message_handler(commands=['BUY', 'buy', 'Buy'])
def buy_handler(message):
    text = "Click on this link: https://ramp-dev.avenirapp.co/#/?type=BUY"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['SELL', 'sell', 'Sell'])
def sell_handler(message):
    text = "Click on this link: https://ramp-dev.avenirapp.co/#/?type=SELL"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")

@bot.message_handler(commands=['Subscribe', 'SUBSCRIBE'])
def subscribe_handler(message):
    text = "Which Trader do you want to view?"
    sent_msg = bot.send_message(message.chat.id, text, reply_markup=genSubscriptionOptions())

@bot.message_handler(func=lambda message: True)
def _all(message):
    send_welcome(message)

def genSubscriptionOptions():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Trader1", url="https://t.me/trader1avenirBot"),
                               InlineKeyboardButton("Trader2", url="https://t.me/trader2avenirBot"), 
                               InlineKeyboardButton("Trader3", url="https://t.me/trader3avenirBot"), 
                               InlineKeyboardButton("Trader4", url="https://t.me/trader4avenirBot"), 
                               InlineKeyboardButton("Trader5", url="https://t.me/trader5avenirBot"), 
                               InlineKeyboardButton("Trader6", url="https://t.me/trader6avenirBot"))
    return markup




bot.infinity_polling()