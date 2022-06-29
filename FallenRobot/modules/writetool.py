import requests
from requests import get
from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from FallenRobot import pbot as fallen, dispatcher, SUPPORT_CHAT


@fallen.on_message(filters.command("write"))
async def handwrite(_, message: Message):
    if not message.reply_to_message:
        text = message.text.split(None, 1)[1]
        m = await fallen.send_message(
            message.chat.id, "**ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**\n\nʟᴇᴍᴍᴇ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ..."
        )
        API = "https://single-developers.up.railway.app/write"
        body = {"text": f"{text}"}
        req = requests.post(
            API, headers={"Content-Type": "application/json"}, json=body
        )
        photo = req.history[1].url
        caption = f"""
sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ʟɪɴᴋ :** `{photo}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{photo}")]]
            ),
        )
        lol = message.reply_to_message.text
        m = await fallen.send_message(
            message.chat.id, "**ᴩʟᴇᴀsᴇ ᴡᴀɪᴛ...**\n\nʟᴇᴍᴍᴇ ᴡʀɪᴛᴇ ɪᴛ ᴏɴ ᴍʏ ᴄᴏᴩʏ..."
        )
        API = "https://single-developers.up.railway.app/write"
        body = {"text": f"{lol}"}
        req = requests.post(
            API, headers={"Content-Type": "application/json"}, json=body
        )
        photo = req.history[1].url
        caption = f"""
sᴜᴄᴄᴇssғᴜʟʟʏ ᴡʀɪᴛᴛᴇɴ ᴛᴇxᴛ 💘

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{dispatcher.bot.first_name}](https://t.me/{dispatcher.bot.username})
🥀 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ :** {message.from_user.mention}
❄ **ʟɪɴᴋ :** `{photo}`
"""
        await m.delete()
        await fallen.send_photo(
            message.chat.id,
            photo=photo,
            caption=caption,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=f"{photo}")]]
            ),
        )


__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__help__ = """

 Writes the given text on white page with a pen 🖊

❍ /write <text> *:* Writes the given text.
 """
