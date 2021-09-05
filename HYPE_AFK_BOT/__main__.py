import importlib
import time
import re
import sys
from termcolor import colored, cprint
from sys import argv
from typing import Optional
from HYPE_AFK_BOT import dispatcher,updater,LOGGER
from AWAY import ALL_MODULES
from MISCL import paginate_modules
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest,ChatMigrated,NetworkError,TelegramError,TimedOut,Unauthorized
from telegram.ext import CallbackContext,CallbackQueryHandler,CommandHandler,Filters,MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop, run_async
from telegram.utils.helpers import escape_markdown
from MISCL.chat_status import *
HYPE_AFK_BOT_IMG = "https://telegra.ph/file/8e5be7f7bd1f93ef370b1.jpg"
IMPORTED = {}
HELPABLE = {}
GDPR = []

for module_name in ALL_MODULES:
    imported_module = importlib.import_module("AWAY." + module_name)
    if not hasattr(imported_module, "__mod_name__"):
        imported_module.__mod_name__ = imported_module.__name__
    if imported_module.__mod_name__.lower() not in IMPORTED:
        IMPORTED[imported_module.__mod_name__.lower()] = imported_module
    if hasattr(imported_module, "__gdpr__"):
        GDPR.append(imported_module)



    
    
LOGGER.info("READY")
updater.start_polling(timeout=15, read_latency=4, drop_pending_updates=True)
main()
updater.idle()
updater.stop()
