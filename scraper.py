import os
import sys
import datetime
from calendar import Calendar
from telegram import Updater
from botconfig import BotConfig
import logging

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)
job_queue = None

modules = None

def start(bot, update):
    moduleStrings = ""
    for module in modules:
        moduleStrings += module.getHelpTitle() + "\n"
        moduleStrings += module.getHelpText() + "\n"

    bot.sendMessage(update.message.chat_id, text=moduleStrings)

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    global job_queue
    global modules

    updater = Updater(BotConfig().getApiToken())
    job_queue = updater.job_queue

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    calendar = Calendar(dp)

    modules = [calendar]

    # on different commands - answer in Telegram
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramCommandHandler("help", start)

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()

