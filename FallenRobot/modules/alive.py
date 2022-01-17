import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from FallenRobot.events import register
from FallenRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/862bf2d97058a6017215b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\nɪ ᴀᴍ ꜰᴀʟʟᴇɴ ʀᴏʙᴏᴛ​.** \n\n"
  TEXT += "» **ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴀʙʏ!** \n\n"
  TEXT += f"» **ᴍʏ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](https://t.me/anonymous_was_bot)** \n\n"
  TEXT += f"» **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"» **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛʜᴀɴᴋs ꜰᴏʀ ᴄʜᴇᴄᴋɪɴɢ 🖤**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/anonymous_0_robot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/DevilsHeavenMF")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
