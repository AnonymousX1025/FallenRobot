from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import telethn as client


@cilent.on_message(filters.command("owner"))
async def start(client, message):
    await message.reply(
            "Here is your gf \nBsdk Girlfriend nahi \nGodFather 😂",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Anonymous", url="https://t.me/anonymous_was_bot")]
                ]
            )
        )

## invisible Module 😂
