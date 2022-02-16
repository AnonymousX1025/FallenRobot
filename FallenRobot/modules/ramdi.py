from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FallenRobot import pbot as fallen


@fallen.on_message(filters.command("Owner"))
async def start(client, message):
    await message.reply(
            "<text>",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(" Anonymous", url="https://t.me/anonymous_was_bot")]
                ]
            )
        )

## invisible Module 😂
