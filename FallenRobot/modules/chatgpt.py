import requests
import json
from Himawari import pgram as app
from pyrogram import filters , client
from pyrogram.types import  Message
from pyrogram.enums import ParseMode



@app.on_message(filters.command("askgpt"), group=765)
async def gpt(_: app, message: Message):
    text = "".join(message.text.split(" ")[1:])
    if len(text) == 0:
        return await message.reply_text(
            "Cannot reply to empty message.", parse_mode=ParseMode.MARKDOWN
        )
    m = await message.reply_text("Getting Request....", parse_mode=ParseMode.MARKDOWN)
    url = "https://api.safone.me/chatgpt"
    payloads = {
          "message": text,
          "chat_mode": "assistant",
          "dialog_messages": "[{\"bot\":\"\",\"user\":\"\"}]"
          }
    headers = {"Content-Type" : "application/json"}
    try:
         response = requests.post(url, json=payloads, headers=headers)
         results = response.json()
         res = results["message"]
         
         await m.edit_text(f"{res}")
    except Exception as e:
         await m.edit_text(f"Error :-\n{e}" )
