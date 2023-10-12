import random

from pyrogram import filters
from pyrogram.types import Message

from FallenRobot import pbot
from FallenRobot.utils.mongo import add_user, is_user, remove_user


@pbot.on_message(filters.command("token") & filters.private)
async def gen_token(_, message: Message):
    chars = "abcdefghijklmnopqrstuvwxyz"
    chars1 = "0123456489"
    gen1 = random.choice(chars)
    gen2 = random.choice(chars)
    gen3 = random.choice(chars1)
    gen4 = random.choice(chars)
    gen5 = random.choice(chars)
    api = f"{message.from_user.id}-fallen-{gen5}{gen1}{gen4}{gen2}{gen3}{gen3}{gen2}{gen4}{gen1}{gen5}"
    if not await is_user(message.from_user.id):
        await add_user(message.from_user.id, api)
        await message.reply_text(
            f"ʜᴇʀᴇ ɪs ʏᴏᴜʀ ᴛᴏᴋᴇɴ ғᴏʀ ғᴀʟʟᴇɴ ᴄʜᴀᴛʙᴏᴛ ᴀᴘɪ :\n<code>{api}</code>\n\n<b>ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴛʜɪs ᴛᴏᴋᴇɴ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.</b>"
        )
    else:
        fallen = await is_user(message.from_user.id)
        await message.reply_text(
            f"ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ɢᴇɴᴇʀᴀᴛᴇᴅ ʏᴏᴜʀ ᴛᴏᴋᴇɴ :\n<code>{fallen}</code>\n\n<b>ᴅᴏɴ'ᴛ sʜᴀʀᴇ ᴛʜɪs ᴛᴏᴋᴇɴ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ ᴇʟsᴇ.</b>"
        )


@pbot.on_message(filters.command("revoke") & filters.private)
async def rev_token(_, message: Message):
    if not await is_user(message.from_user.id):
        return await message.reply_text(
            f"ʟᴏᴏᴋs ʟɪᴋᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴛᴏᴋᴇɴ ʙᴇғᴏʀᴇ."
        )
    fallen = await is_user(message.from_user.id)
    await remove_user(message.from_user.id, fallen)
    await message.reply_text(
        f"<b>ғᴀʟʟᴇɴ ᴄʜᴀᴛʙᴏᴛ ᴀᴘɪ ᴛᴏᴋᴇɴ ʀᴇᴠᴏᴋᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ.</b>\n\nʏᴏᴜ ᴄᴀɴ ɢᴇɴᴇʀᴀᴛᴇ ʏᴏᴜʀ ᴛᴏᴋᴇɴ ᴀɢᴀɪɴ ʙʏ /token"
    )
