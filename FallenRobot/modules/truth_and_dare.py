import html
import random
import FallenRobot.modules.truth_and_dare_string as truth_and_dare_string
from FallenRobot import dispatcher
from telegram import ParseMode, Update, Bot
from FallenRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async


def truth(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))


def dare(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__help__ = """
*Truth & Dare*
 ❍ /truth *:* Sends a random truth string.
 ❍ /dare *:* Sends a random dare string.
"""
__mod_name__ = "Tʀᴜᴛʜ-Dᴀʀᴇ"
