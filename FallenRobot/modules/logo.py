from pyrogram import filters
from pyrogram.types import Message
from requests import get
from pyrogram import client
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FallenRobot import pbot as app
from FallenRobot.sample_config import API_ID, API_HASH, BOT_TOKEN

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

app = client("Fallen Robot", bot_token = BOT_TOKEN, api_id = API_ID, api_hash = API_HASH)

app.run()

caption = """
» ʟᴏɢᴏ sᴜᴄᴄᴇssꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙᴀʙʏ​ «
◇───────────────◇
💔 **ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ** : [ᴀɴᴏɴʏᴍᴏᴜs](https://t.me/anonymous_0_robot)
😇 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ​** : {}
💕 **ᴘᴏᴡᴇʀᴇᴅ ʙʏ​ **  : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](https://t.me/anonymous_was_bot)
◇───────────────◇️  
    """
#logo creator
@app.on_message(filters.command("logo"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://single-developers.herokuapp.com/logo?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
#hq logo creator
@app.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/logohq?name={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )

#handwrite
@app.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    API = "https://api.single-developers.software/write"
    body = {     
     "text":f"{text}"     
    }
    req = requests.post(API, headers={'Content-Type': 'application/json'}, json=body)
    img = req.history[1].url
    await app.send_photo(message.chat.id, photo=img, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{img}"
                    )
                ]
            ]
          ),
    )

#wallpaper
@app.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    text = message.text.split(None, 1)[1]
    photo = get(f"https://api.single-developers.software/wallpaper?search={text}").history[1].url
    await app.send_photo(message.chat.id, photo=photo, caption=caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{photo}"
                    )
                ]
            ]
          ),
    )
