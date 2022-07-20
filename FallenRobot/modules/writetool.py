import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from FallenRobot import pbot as fallen, dispatcher, SUPPORT_CHAT


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        name = (
            message.text.split(None, 1)[1]
            if len(message.command) < 3
            else message.text.split(None, 1)[1].replace(" ", "%20")
        )
        m = await fallen.send_message(
            message.chat.id, "**ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**\n\nʟᴇᴍᴍᴇ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ..."
        )
        photo = "https://apis.xditya.me/write?text=" + name
        caption = f"""
sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• sᴜᴩᴩᴏʀᴛ •", url=f"https://t.me/{SUPPORT_CHAT}"
                        )
                    ]
                ]
            ),
        )
        await m.delete()
    else:
        lol = message.reply_to_message.text
        name = lol.split(None, 0)[0].replace(" ", "%20")
        m = await fallen.send_message(
            message.chat.id, "**ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**\n\nʟᴇᴍᴍᴇ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ..."
        )
        photo = "https://apis.xditya.me/write?text=" + name
        caption = f"""
sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
"""
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "• sᴜᴩᴩᴏʀᴛ •", url=f"https://t.me/{SUPPORT_CHAT}"
                        )
                    ]
                ]
            ),
        )
        await m.delete()


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """

 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
 """
