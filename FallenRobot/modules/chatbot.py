from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
from FallenRobot import API_ID, API_HASH, TOKEN, MONGO_DB_URI
import requests
import os
import re


API_ID = API_ID 
API_HASH = API_HASH 
BOT_TOKEN = TOKEN
MONGO_URL = MONGO_DB_URI


bot = Client(
    "Fallen" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]


@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-", "~", "•", "*"])
    & ~filters.private)
async def addchat(_, message): 
    kukidb = MongoClient(MONGO_URL)
    
    kuki = kukidb["KukiDb"]["Kuki"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_kuki = kuki.find_one({"chat_id": message.chat.id})
    if not kuki:
        toggle.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"» Successfully Activated\nFallenXRobot @{message.chat.username}\n Activated by [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n© @DevilsHeavenMF")
    else:
        await message.reply_text(f"FallenXRobot already activated in @{message.chat.username}")


@bot.on_message(
    filters.command("removechat", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def rmchat(_, message): 
    kukidb = MongoClient(MONGO_URL)
    
    kuki = kukidb["KukiDb"]["Kuki"] 
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_kuki = kuki.find_one({"chat_id": message.chat.id})
    if not is_kuki:
        await message.reply_text("FallenXRobot ChatBot is already disabled.")
    else:
        kuki.delete_one({"chat_id": message.chat.id})
        await message.reply_text("» FallenXRobot ChatBot disabled !")


@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  kukidb = MongoClient(MONGO_URL)
    
  kuki = kukidb["KukiDb"]["Kuki"] 

  is_kuki = kuki.find_one({"chat_id": message.chat.id})
  if is_kuki:

      Kuki =   requests.get(f"https://kukiapi.xyz/api/message={msg}").json()

      moezilla = f"{Kuki['reply']}"

      self = await bot.get_me()
      bot_id = self.id
      if not message.reply_to_message.from_user.id == bot_id:
          return
      
      await client.send_chat_action(message.chat.id, "typing")
      await message.reply_text(moezilla)


@bot.on_message(
    filters.text
    & ~filters.reply
    & filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/message={msg}").json()

  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


@bot.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def kukiai(client: Client, message: Message):

  msg = message.text.replace(message.text.split(" ")[0], "")
    
  Kuki =   requests.get(f"https://kukiapi.xyz/api/message={msg}").json()

  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)

bot.run()

__help__ = """
*Admins only Commands*:
  »  /chatbot *:* Shows chatbot control panel

"""

__mod_name__ = "Cʜᴀᴛʙᴏᴛ"


CHATBOTK_HANDLER = CommandHandler("chatbot", kuki )
ADD_CHAT_HANDLER = CallbackQueryHandler(kukiadd, pattern=r"add_chat" )
RM_CHAT_HANDLER = CallbackQueryHandler(kukirm, pattern=r"rm_chat" )
CHATBOT_HANDLER = MessageHandler(
    Filters.text & (~Filters.regex(r"^#[^\s]+") & ~Filters.regex(r"^!")
                    & ~Filters.regex(r"^\/")), chatbot, )
LIST_ALL_CHATS_HANDLER = CommandHandler(
    "allchats", list_all_chats, filters=CustomFilters.dev_filter, )

dispatcher.add_handler(ADD_CHAT_HANDLER)
dispatcher.add_handler(CHATBOTK_HANDLER)
dispatcher.add_handler(RM_CHAT_HANDLER)
dispatcher.add_handler(LIST_ALL_CHATS_HANDLER)
dispatcher.add_handler(CHATBOT_HANDLER)

__handlers__ = [
    ADD_CHAT_HANDLER,
    CHATBOTK_HANDLER,
    RM_CHAT_HANDLER,
    LIST_ALL_CHATS_HANDLER,
    CHATBOT_HANDLER,
]
