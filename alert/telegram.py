from telegram.ext import Updater
import os

bot_authtoken = os.environ.get("telegram_auth_token")

updater = Updater(token=bot_authtoken)