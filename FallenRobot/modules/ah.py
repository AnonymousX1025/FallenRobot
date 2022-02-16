from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from FallenRobot import pbot as client


@client.on_message(filters.command("dev"))
async def start(client, message):
    await message.reply(
            "ʜᴇʏ\n  ɪ ᴀᴍ 𝗙𝝙𝗟𝗟𝝣𝗡 ✘ 𝗥𝗢𝗕𝗢𝗧\n    ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ ɪs​‌ [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](tg://user?id=1356469075)",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("✗ 𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦 ✗", url="https://t.me/anonymous_was_bot")]
                ]
            )
        )

## Ramdi Module  😂
__mod_name__ = "Ramdi"
