import logging
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from mpv import MPV

# logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

mpv = MPV(ytdl=True, vo='null')

def start(update, context):
    update.message.reply_text("yo!")

def play(update, context):
    mpv.play(update.message.text)

def main():
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <token>")
        exit(1)

    updater = Updater(sys.argv[1], use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, play))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
