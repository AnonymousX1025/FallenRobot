 import os

import requests
import wget
from pyrogram import filters

from FallenRobot import pbot as Jebot
from FallenRobot.pyrogramee.dark import get_arg


@Jebot.on_message(filters.command("saavn"))
async def song(client, message):
    message.chat.id
    message.from_user["id"]
    args = get_arg(message) + " " + "song"
    if args.startswith(" "):
        await message.reply("<b>Enter song name baby❗</b>")
        return ""
    m = await message.reply_text(
        "Downloading your song,\nPlease wait...⏳️"
    )
    try:
        r = requests.get(f"https://snobybuddymusic.herokuapp.com/result/?query={args}")
    except Exception as e:
        await m.edit(str(e))
        return
    sname = r.json()[0]["song"]
    slink = r.json()[0]["media_url"]
    ssingers = r.json()[0]["singers"]
    file = wget.download(slink)
    ffile = file.replace("mp4", "m4a")
    os.rename(file, ffile)
    await message.reply_audio(audio=ffile, title=sname, performer=ssingers)
    os.remove(ffile)
    await m.delete()
