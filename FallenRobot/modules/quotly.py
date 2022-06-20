from io import BytesIO
from traceback import format_exc

from pyrogram import filters
from pyrogram.types import Message

from FallenRobot import arq
from FallenRobot.utils.errors import capture_err
from FallenRobot import pbot as app


async def quotify(messages: list):
    response = await arq.quotly(messages)
    if not response.ok:
        return [False, response.result]
    sticker = response.result
    sticker = BytesIO(sticker)
    sticker.name = "sticker.webp"
    return [True, sticker]


def getArg(message: Message) -> str:
    arg = message.text.strip().split(None, 1)[1].strip()
    return arg


def isArgInt(message: Message) -> bool:
    count = getArg(message)
    try:
        count = int(count)
        return [True, count]
    except ValueError:
        return [False, 0]


@app.on_message(filters.command("q"))
@capture_err
async def quotly_func(client, message: Message):
    if not message.reply_to_message:
        return await message.reply_text("Rᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ǫᴜᴏᴛᴇ ɪᴛ.")
    if not message.reply_to_message.text:
        return await message.reply_text("Rᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ʜᴀs ɴᴏ ᴛᴇxᴛ, ᴄᴀɴ'ᴛ ǫᴜᴏᴛᴇ ɪᴛ .")
    m = await message.reply_text("Quoting Messages Please wait....")
    if len(message.command) < 2:
        messages = [message.reply_to_message]

    elif len(message.command) == 2:
        arg = isArgInt(message)
        if arg[0]:
            if arg[1] < 2 or arg[1] > 10:
                return await m.edit("Aʀɢᴜᴍᴇɴᴛ ᴍᴜsᴛ ʙᴇ ʙᴇᴛᴡᴇᴇɴ 2-10.")
            count = arg[1]
            messages = await client.get_messages(
                message.chat.id,
                [
                    i
                    for i in range(
                        message.reply_to_message.message_id,
                        message.reply_to_message.message_id + count,
                    )
                ],
                replies=0,
            )
        else:
            if getArg(message) != "r":
                return await m.edit(
                    "Incorrect Argument, Pass **'r'** or **'INT'**, **EX:** __/q 2__"
                )
            reply_message = await client.get_messages(
                message.chat.id,
                message.reply_to_message.message_id,
                replies=1,
            )
            messages = [reply_message]
    else:
        await m.edit("Iɴᴄᴏʀʀᴇᴄᴛ ᴀʀɢᴜᴍᴇɴᴛ, ᴄʜᴇᴄᴋ ǫᴜᴏᴛʟʏ ᴍᴏᴅᴜʟᴇ ɪɴ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ.")
        return
    try:
        sticker = await quotify(messages)
        if not sticker[0]:
            await message.reply_text(sticker[1])
            return await m.delete()
        sticker = sticker[1]
        await message.reply_sticker(sticker)
        await m.delete()
        sticker.close()
    except Exception as e:
        await m.edit(
            "Sᴏᴍᴇᴛʜɪɴɢ ᴡʀᴏɴɢ ʜᴀᴘᴘᴇɴᴇᴅ ᴡʜɪʟᴇ ǫᴜᴏᴛɪɴɢ ᴍᴇssᴀɢᴇs,"
            + " Tʜɪs ᴇʀʀᴏʀ ᴜsᴜᴀʟʟʏ ʜᴀᴘᴘᴇɴs ᴡʜᴇɴ ᴛʜᴇʀᴇ's ᴀ "
            + " ᴍᴇssᴀɢᴇ ᴄᴏɴᴛᴀɪɴɪɴɢ sᴏᴍᴇᴛʜɪɴɢ ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴛᴇxᴛ."
        )
        e = format_exc()
        print(e)
