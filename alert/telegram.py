from telegram.ext import Updater
import os
import logging

bot_authtoken = os.environ.get("telegram_auth_token")

updater = Updater(token=bot_authtoken)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update: Update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello World from Bot")