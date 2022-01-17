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
  TEXT = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Fallen Robot.** \n\n"
  TEXT += "⚪ **I'm alive** \n\n"
  TEXT += f"⚪ **My Master : [Zaid](https://t.me/Timesisnotwaiting)** \n\n"
  TEXT += f"⚪ **Library Version :** `{telever}` \n\n"
  TEXT += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here 🖤**"
  BUTTON = [[Button.url("Help", "https://t.me/anonymous_0_robot?start=help"), Button.url("Support", "https://t.me/DevilsHeavenMF")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
