from pyrogram import filters
from pyrogram.types import Message
from FallenRobot import pbot as app
from requests import get
import os
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied
from PIL import Image
import io

caption = """
» ʟᴏɢᴏ sᴜᴄᴄᴇssꜰᴜʟʟʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʙᴀʙʏ​ «
`◇───────────────◇`
💔 **ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ ** : [ᴀɴᴏɴʏᴍᴏᴜs](https://t.me/FallenXRobot)
😇 **ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ ​** : {}
💕 **ᴘᴏᴡᴇʀᴇᴅ ʙʏ​ **  : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](https://t.me/anonymous_was_bot)
`◇───────────────◇️  `
    """
JOIN_ASAP = f" **🚫 Access Denied**\n\n You have to join [My Group](https://t.me/DevilsHeavenMF) to use me. So, please join it & Try Again." 
FSUBB = InlineKeyboardMarkup( 
           [[ 
               InlineKeyboardButton(text="• Group • ", url=f"https://t.me/DevilsHeavenMF") 
           ]] 
)

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

#logo creator
@app.on_message(filters.command("logo") & ~filters.bot)
async def logo(client, message):      
 try:
        await message._client.get_chat_member(int("-1001686672798"), message.from_user.id)
 except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return    
 quew = get_text(message)
 if not quew:
     await client.send_message(message.chat.id, "😶 **Please Give me A Text For The Logo**.")
     return
 m = await client.send_message(message.chat.id, "`🙂 Creating Your Logo...`")
 try:
    text = get_text(message)
    LOGO_API = f"https://api.single-developers.software/logo?name={text}"
    randc = (LOGO_API)
    img = Image.open(io.BytesIO(requests.get(randc).content))
    murl = requests.get(f"https://api.single-developers.software/logo?name={text}").history[1].url
    fname = "anonymous.png"
    img.save(fname, "png")
    await client.send_photo(message.chat.id, photo=murl, caption = caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{murl}"
                    )
                ],
            ]
          ),
    )
    if os.path.exists(fname):
            os.remove(fname)
 except Exception as e:
    await client.send_message(message.chat.id, f'Error, Report @DevilsHeavenMF, {e}')
    await m.delete()

#hq logo creator
@app.on_message(filters.command("logohq"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001686672798"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m = await app.send_message(message.chat.id, "`⚙️ Creating Your Logo...`")
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
    await m.delete()
#handwrite
@app.on_message(filters.command("write"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001686672798"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m = await app.send_message(message.chat.id, "`⚙️ Writing Your text...`")
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
    await m.delete()
#wallpaper
@app.on_message(filters.command("wall"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001686672798"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    text = message.text.split(None, 1)[1]
    m=await app.send_message(message.chat.id, "`⚙️ Searching Your Wall...`")
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
    await m.delete()
#slogo
@app.on_message(filters.command("glogo"))
async def on_off_antiarab(_, message: Message):
    try:
        await message._client.get_chat_member(int("-1001686672798"), message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
        text=JOIN_ASAP, disable_web_page_preview=True, reply_markup=FSUBB
    )
        return 
    quew = get_text(message)
    if not quew:
        await message.reply_text(message.chat.id, "😶Please give a text.")
        return
    m = await app.send_message(message.chat.id, "`⚙️ Creating Your Logo...`")    
    name = message.text.split(None, 1)[1]
    req = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}")
    IMG = req.text
    rurl = requests.get(f"https://sd-logo-api.herokuapp.com/?logo={name}").text    
    await app.send_photo(message.chat.id, photo=IMG, caption =caption.format(message.from_user.mention),
                 reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•• ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ​ ••", url=f"{rurl}"
                    )
                ]
            ]
          ),
    )
    await m.delete()

__f__ = """
**Create Beautiful logos for your profile pictures from Fallen.**
×  /logo [TEXT]: Create a logo 
×  /logohq [TEXT]: Create a HQ logo 
×  /write [TEXT] : hand writer
×  /wall [TEXT] : search wallpapers
×  /slogo [TEXT] : New Beautiful trending logo


Logo Maker is Powered by @SingleDevelopers & @MrItzme
 """
__mod_name__ = Lavda
