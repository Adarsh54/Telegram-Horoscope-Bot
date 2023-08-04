#main.py
import os
import telegram
import asyncio
import requests
    
    
async def choosePath(bot, messageFile):
    messageId = messageFile['message']['chat']['id']
    text = messageFile['message']['text']
    if text == "BUY" or text == "Buy":
        await bot.sendMessage(chat_id=messageId, text="Click on this link: https://ramp-dev.avenirapp.co/#/?type=BUY", parse_mode=None)
    elif text == "SELL" or text == "Sell":
        await bot.sendMessage(chat_id=messageId, text="Click on this link: https://ramp-dev.avenirapp.co/#/?type=SELL", parse_mode=None)
    elif text == "SUBSCRIBE" or text == "Subscribe":
        await bot.sendMessage(chat_id=messageId, text="Clink the link the below to access our trading channel!", parse_mode=None)
        await bot.sendMessage(chat_id=messageId, text="https://t.me/+lsr2tcZdvvUyYzlh", parse_mode=None)
    else: 
        await bot.sendMessage(chat_id=messageId, text="Welcome to Avenir! Would you like to buy or sell crypto? Type BUY for buy, SELL for sell, or SUBSCRIBE to view our trader subscription options.", parse_mode=None)

def telegram_bot(request):
    """Main function."""
    bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
    print(request.method)
    if request.method == "POST":
        messageFile = request.get_json()
        for key, value in messageFile.items():
	        print(value, key)
        asyncio.run(choosePath(bot, messageFile))
        # Get the last update.
    return "okay"
