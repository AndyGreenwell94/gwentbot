from uuid import uuid4
import sys
import os
import re
from database import Cards, Session
from telegram import ParseMode, InlineQueryResultPhoto
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
session = Session()


def start(bot, update):
    update.message.reply_text('Hello, I can send you any card form Gwent,'
                              ' but you should ask for it via inline query. Like this @gwent_card_bot Ciri')


def help(bot, update):
    update.message.reply_text('I can send you any card form Gwent,'
                              ' but you should ask for it via inline query. Like this @gwent_card_bot Ci')


def escape_markdown(text):
    """Helper function to escape telegram markup symbols"""
    escape_chars = '\*_`\['
    return re.sub(r'([%s])' % escape_chars, r'\\\1', text)


def inlinequery(bot, update):
    query = update.inline_query.query
    r = session.query(Cards).filter(Cards.name.like('%'+query+'%')).all()
    results = list([InlineQueryResultPhoto(id=uuid4(), title=x.name, thumb_url=x.image, photo_url=x.image,
                                           caption=x.name+'\n'+x.text, parse_mode=ParseMode.MARKDOWN) for x in r[:10]])

    update.inline_query.answer(results)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    TOKEN = os.environ.get('TOKEN')
    PORT = int(os.environ.get('PORT', '5000'))
    updater = Updater(TOKEN)

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.setWebhook("https://gwentbot.herokuapp.com/" + TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(InlineQueryHandler(inlinequery))

    dp.add_error_handler(error)

    updater.idle()


if __name__ == '__main__':
    main()