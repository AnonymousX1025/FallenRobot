import io
from FallenRobot.events import register
from FallenRobot import telethn as tbot
from telethon import types
from telethon import events
from telethon.tl import functions
from telethon.tl.types import *


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):
        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    if isinstance(chat, types.InputPeerUser):
        return True


@register(pattern="^/json$")
async def _(event):
    if event.fwd_from:
        return
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply(
                "🥴 ɴᴇᴇᴅ ᴀᴅᴍɪɴ ᴩᴏᴡᴇʀ ᴛᴏ ᴜsᴇ ᴛʜɪs ɪɴ ɢʀᴏᴜᴩs﹐ ʙᴜᴛ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ɪᴛ ɪɴ ᴍʏ ᴩᴍ."
            )
            return

    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    if len(the_real_message) > 4095:
        with io.BytesIO(str.encode(the_real_message)) as out_file:
            out_file.name = "json.text"
            await tbot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                reply_to=reply_to_id,
            )
            await event.delete()
    else:
        await event.reply("`{}`".format(the_real_message))
