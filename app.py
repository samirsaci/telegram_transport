# .\venv\Scripts\activate
import logging
import os
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater, CommandHandler, MessageHandler, Filters, ConversationHandler, CallbackContext
)

from mail import *
import requests



# Token provided by @ BotFather
TOKEN = 'TOKEN' 
# Your Heroku App Page 
APP_NAME = 'https://XXXX.herokuapp.com/'
# Port
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Functions
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''Hello ! I am your shipment tracking bot, please find below commands to interract with me. \n /start_tracking: start tracking process''')
# Location Tracking
LOC, DN, PHOTO = range(3)

def start_tracking(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Driver: %s", user.first_name)
    update.message.reply_text(
        'Please share your current GPS location.',
        reply_markup = ReplyKeyboardRemove(),
    )

    return LOC

def photo(update: Update, context: CallbackContext):
    user = update.message.from_user
    photo_file = update.message.photo[-1].get_file()
    # photo_file.download('user_photo.jpg')

    # Get link to get file_path
    link1 = "https://api.telegram.org/bot{}/getfile?file_id={}".format(TOKEN, photo_file.file_id)
    r = requests.get(link1)
    file_path = r.json()["result"]["file_path"]

    # Link to download file
    link2 = "https://api.telegram.org/file/bot{}/{}".format(TOKEN, file_path)
    global img_link
    img_link = link2
    logger.info("Picture: %s", img_link)

    mail(gps_location, delivery_number, img_link)
    update.message.reply_text('A picture of your shipment has been uploaded. Thank you for your cooperation.')
    return ConversationHandler.END

def location(update: Update, context: CallbackContext):
    user = update.message.from_user
    user_location = update.message.location
    logger.info("Driver ID location %s: (%s, %s)", user.first_name, user_location.latitude, user_location.longitude)
    global gps_location
    gps_location = "({}, {})".format(user_location.latitude, user_location.longitude)
    update.message.reply_text('Your current GPS location has been recorded. Please enter delivery number.')
    return DN


def delivery_number(update: Update, context: CallbackContext):
    user = update.message.from_user
    global delivery_number
    delivery_number = update.message.text
    logger.info("Delivery Number: %s", delivery_number)
    update.message.reply_text('Delivery number is now recorded. Please upload a picture of your shipment.')

    return PHOTO

def cancel(update: Update, context: CallbackContext):
    user = update.message.from_user
    logger.info("Driver ID %s decided to cancel location record.", user.first_name, update.message.text)

    update.message.reply_text('Location record has been cancelled.')

    return ConversationHandler.END

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    '''Start Bot'''
    # Launch Updater
    updater = Updater("{}".format(TOKEN), use_context=True)
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # conversions handled by command
    dispatcher.add_handler(CommandHandler("start", start))

    # conversation handler
    loc_handler = ConversationHandler(
        entry_points = [CommandHandler('start_tracking', start_tracking)],
        states = {
            LOC: [
                MessageHandler(Filters.location, location)],
            PHOTO: [
                MessageHandler(Filters.photo, photo)],
            DN:[MessageHandler(Filters.text & ~Filters.command, delivery_number)]
        },
        fallbacks = [CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(loc_handler)

    # log all errors
    dispatcher.add_error_handler(error)
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path="{}".format(TOKEN))
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook("{}".format(APP_NAME) + "{}".format(TOKEN))
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()