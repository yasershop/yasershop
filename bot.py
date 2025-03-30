import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Function to get gold price
def get_gold_price():
    url = "https://api.metals-api.com/v1/latest?access_key=YOUR_API_KEY&base=USD&symbols=XAU"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["XAU"]

# Command handler function to show gold price
def gold_price(update: Update, context: CallbackContext) -> None:
    price = get_gold_price()
    update.message.reply_text(f"The current gold price is {price} USD per ounce.")

# Main function to start the bot
def main():
    updater = Updater(os.getenv("TELEGRAM_TOKEN"))
    
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("gold", gold_price))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()