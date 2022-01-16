# 🙈 Give me ⭐️ before kanging code
# © @AnonymousBoy1025 🌚

import requests
url = "https://iamai.p.rapidapi.com/ask"
from FallenRobot import telethn, OWNER_ID
from FallenRobot.events import register
from telethon import events
from telethon import types
from telethon.tl import functions
import asyncio, os

@register(pattern="Fallen (.*)")
async def hmm(event):
  test = event.pattern_match.group(1)
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if "no no" in result:
   pro = "I am fairly found and I was made by @anonymous_was_bot."
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "ann" in result:
   pro = "My name is Fallen"
   try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    try:
      async with telethn.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(result)
    except CFError as e:
           print(e)
