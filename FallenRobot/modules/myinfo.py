import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from FallenRobot import telethn as bot
from FallenRobot import telethn as tgbot
from FallenRobot.events import register

edit_time = 5
""" =======================FALLEN ROBOT====================== """
file1 = "https://telegra.ph/file/9a85d0a873e2dd80d278d.jpg"
file2 = "https://telegra.ph/file/9e7815284031452afa9e5.jpg"
file3 = "https://telegra.ph/file/dcc5e003287f69acea368.jpg"
file4 = "https://telegra.ph/file/ed1ce7fee94f46b0f671e.jpg"
file5 = "https://telegra.ph/file/701028ce085ecfa961a36.jpg"
""" =======================FALLEN ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("information", data="informations")]]
    on = await bot.send_file(
        event.chat_id,
        file=file2,
        caption=f"Hey {firstname}, \n Click on the button below \n to get info about you",
        buttons=button,
    )

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)

    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
    try:
        boy = event.sender_id
        PRO = await bot.get_entity(boy)
        LILIE = "POWERED BY 𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦 \n\n"
        LILIE += f"FIRST NAME : {PRO.first_name} \n"
        LILIE += f"LAST NAME : {PRO.last_name}\n"
        LILIE += f"YOU BOT : {PRO.bot} \n"
        LILIE += f"RESTRICTED : {PRO.restricted} \n"
        LILIE += f"USER ID : {boy}\n"
        LILIE += f"USERNAME : {PRO.username}\n"
        await event.answer(LILIE, alert=True)
    except Exception as e:
        await event.reply(f"{e}")


__command_list__ = ["myinfo"]
