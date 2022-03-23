#credit @Shubhanshutya AMANTYA1
import asyncio
from pyrogram import filters
from FallenRobot import pbot as app
from pyrogram.types import Message
from FallenRobot import eor
from FallenRobot.utils.errors import capture_err

active_channel = []

async def channel_toggle(db, message: Message):
    status = message.text.split(None, 1)[1].lower()
    chat_id = message.chat.id
    if status == "on":
        if chat_id not in db:
            db.append(chat_id)
            text = "**Anti Channel Mode `enabled` ✅. I will delete all message that send with channel names. Dare to leap**"
            return await eor(message, text=text)
        await eor(message, text="antichannel Is Already Enabled.")
    elif status == "off":
        if chat_id in db:
            db.remove(chat_id)
            return await eor(message, text="antichannel Disabled!")
        await eor(message, text=f"**Anti Channel Mode Successfully Deactivated In The Chat** {message.chat.id} ❌")
    else:
        await eor(message, text="I undestand `/antichannel on` and `/antichannel off` only")


# Enabled | Disable antichannel


@app.on_message(filters.command("antichannel") & ~filters.edited)
@capture_err
async def antichannel_status(_, message: Message):
    if len(message.command) != 2:
        return await eor(message, text="I undestand `/antichannel on` and `/antichannel off` only")
    await channel_toggle(active_channel, message)



@app.on_message(
    (
        filters.document
        | filters.photo
        | filters.sticker
        | filters.animation
        | filters.video
        | filters.text
    )
    & ~filters.private,
    group=41,
)
async def anitchnl(_, message):
  chat_id = message.chat.id
  if message.sender_chat:
    sender = message.sender_chat.id 
    if message.chat.id not in active_channel:
        return
    if chat_id == sender:
        return
    else:
        await message.delete()
        ti = await message.reply_text("**A anti-channel message detected. I deleted it..!**")
        await asyncio.sleep(7)
        await ti.delete()        

__Mod_Name__ = "Anti-Channel"
__Help__ = """
your groups to stop anonymous channels sending messages into your chats.
**Type of messages**
        - document
        - photo
        - sticker
        - animation
        - video
        - text
        
**Admin Commands:**
 - /antichannel [on / off] - Anti- channel  function 
**Note** : If linked_channel  send any containing characters in this type when on  function no del    
 """
