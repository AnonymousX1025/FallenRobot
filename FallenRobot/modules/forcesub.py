import logging
import time

from pyrogram import filters
from pyrogram.errors.exceptions.bad_request_400 import (
    ChatAdminRequired,
    PeerIdInvalid,
    UsernameNotOccupied,
    UserNotParticipant,
)
from pyrogram.types import ChatPermissions, InlineKeyboardButton, InlineKeyboardMarkup

from FallenRobot import DRAGONS as SUDO_USERS
from FallenRobot import pbot
from FallenRobot.modules.sql import forceSubscribe_sql as sql


logging.basicConfig(level=logging.INFO)

static_data_filter = filters.create(
    lambda _, __, query: query.data == "onUnMuteRequest"
)


@pbot.on_callback_query(static_data_filter)
def _onUnMuteRequest(client, cb):
    user_id = cb.from_user.id
    chat_id = cb.message.chat.id
    chat_db = sql.fs_settings(chat_id)
    if chat_db:
        channel = chat_db.channel
        chat_member = client.get_chat_member(chat_id, user_id)
        if chat_member.restricted_by:
            if chat_member.restricted_by.id == (client.get_me()).id:
                try:
                    client.get_chat_member(channel, user_id)
                    client.unban_chat_member(chat_id, user_id)
                    cb.message.delete()
                    # if cb.message.reply_to_message.from_user.id == user_id:
                    # cb.message.delete()
                except UserNotParticipant:
                    client.answer_callback_query(
                        cb.id,
                        text=f"» ᴊᴏɪɴ @{channel} ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴛʜᴇɴ ᴩʀᴇss 'ᴜɴᴍᴜᴛᴇ ᴍᴇ' ʙᴜᴛᴛᴏɴ.",
                        show_alert=True,
                    )
            else:
                client.answer_callback_query(
                    cb.id,
                    text="» ʏᴏᴜ ᴀʀᴇ ᴍᴜᴛᴇᴅ ʙʏ ᴀᴅᴍɪɴs ғᴏʀ ᴀɴᴏᴛʜᴇʀ ʀᴇᴀsᴏɴ sᴏ ɪ ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ʏᴏᴜ.",
                    show_alert=True,
                )
        else:
            if (
                not client.get_chat_member(chat_id, (client.get_me()).id).status
                == "administrator"
            ):
                client.send_message(
                    chat_id,
                    f"» **{cb.from_user.mention} ɪs ᴛʀʏɪɴɢ ᴛᴏ ᴜɴᴍᴜᴛᴇ ʜɪᴍsᴇʟғ ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ʜɪᴍ ʙᴇᴄᴀᴜsᴇ ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**\n__#ʟᴇᴀᴠɪɴɢ ᴄʜᴀᴛ...__",
                )

            else:
                client.answer_callback_query(
                    cb.id,
                    text="» ᴡᴀʀɴɪɴɢ ! ᴅᴏɴ'ᴛ ᴩʀᴇss ᴛʜᴇ ᴜɴᴍᴜᴛᴇ ʙᴜᴛᴛᴏɴ ᴡʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ.",
                    show_alert=True,
                )


@pbot.on_message(filters.text & ~filters.private, group=1)
def _check_member(client, message):
    chat_id = message.chat.id
    chat_db = sql.fs_settings(chat_id)
    if chat_db:
        user_id = message.from_user.id
        if (
            not client.get_chat_member(chat_id, user_id).status
            in ("administrator", "creator")
            and not user_id in SUDO_USERS
        ):
            channel = chat_db.channel
            try:
                client.get_chat_member(channel, user_id)
            except UserNotParticipant:
                try:
                    sent_message = message.reply_text(
                        "ʜᴇʏ {} 💔 \n **ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ᴊᴏɪɴᴇᴅ @{} ᴄʜᴀɴɴᴇʟ ʏᴇᴛ**🧐 \n \nᴩʟᴇᴀsᴇ ᴊᴏɪɴ [ᴛʜɪs ᴄʜᴀɴɴᴇʟ](https://t.me/{}) ᴀɴᴅ ᴛʜᴇɴ ᴩʀᴇss ᴛʜᴇ **ᴜɴᴍᴜᴛᴇ ᴍᴇ** ʙᴜᴛᴛᴏɴ. \n \n ".format(
                            message.from_user.mention, channel, channel
                        ),
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [
                                [
                                    InlineKeyboardButton(
                                        "• ᴄʜᴀɴɴᴇʟ •",
                                        url="https://t.me/{}".format(channel),
                                    )
                                ],
                                [
                                    InlineKeyboardButton(
                                        "• ᴜɴᴍᴜᴛᴇ ᴍᴇ •", callback_data="onUnMuteRequest"
                                    )
                                ],
                            ]
                        ),
                    )
                    client.restrict_chat_member(
                        chat_id, user_id, ChatPermissions(can_send_messages=False)
                    )
                except ChatAdminRequired:
                    sent_message.edit(
                        "😕 **ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ʜᴇʀᴇ...**\n__ɢɪᴠᴇ ᴍᴇ ᴩᴇʀᴍɪssɪᴏɴs ᴛᴏ ʙᴀɴ ᴜsᴇʀs ᴀɴᴅ ᴛʜᴇɴ ᴛʀʏ ᴀɢᴀɪɴ... \n#ᴇɴᴅɪɴɢ ғsᴜʙ...__"
                    )

            except ChatAdminRequired:
                client.send_message(
                    chat_id,
                    text=f"😕 **ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ @{channel} ᴄʜᴀɴɴᴇʟ.**\n__ᴩʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.\n#ᴇɴᴅɪɴɢ ғsᴜʙ...__",
                )


@pbot.on_message(filters.command(["forcesubscribe", "fsub"]) & ~filters.private)
def config(client, message):
    user = client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status == "creator" or user.user.id in SUDO_USERS:
        chat_id = message.chat.id
        if len(message.command) > 1:
            input_str = message.command[1]
            input_str = input_str.replace("@", "")
            if input_str.lower() in ("off", "no", "disable"):
                sql.disapprove(chat_id)
                message.reply_text("**» sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ.**")
            elif input_str.lower() in ("clear"):
                sent_message = message.reply_text(
                    "**» ᴜɴᴍᴜᴛɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴍᴜᴛᴇᴅ ʙʏ ɴᴏᴛ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ...**"
                )
                try:
                    for chat_member in client.get_chat_members(
                        message.chat.id, filter="restricted"
                    ):
                        if chat_member.restricted_by.id == (client.get_me()).id:
                            client.unban_chat_member(chat_id, chat_member.user.id)
                            time.sleep(1)
                    sent_message.edit(
                        "**» ᴜɴᴍᴜᴛᴇᴅ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴡʜᴏ ᴀʀᴇ ᴍᴜᴛᴇᴅ ʙʏ ᴍᴇ ғᴏʀ ɴᴏᴛ ᴊᴏɪɴɪɴɢ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ.**"
                    )
                except ChatAdminRequired:
                    sent_message.edit(
                        "😕 **ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**\n__ɪ ᴄᴀɴ'ᴛ ᴜɴᴍᴜᴛᴇ ᴍᴇᴍʙᴇʀs ʙᴇᴄᴀᴜsᴇ ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴩᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴍᴜᴛᴇ/ᴜɴᴍᴜᴛᴇ ᴜsᴇʀs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.__"
                    )
            else:
                try:
                    client.get_chat_member(input_str, "me")
                    sql.add_channel(chat_id, input_str)
                    message.reply_text(
                        f"**» ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ ᴇɴᴀʙʟᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ**\n__ғᴏʀᴄᴇ sᴜʙ ᴇɴᴀʙʟᴇᴅ, ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴩ ᴍᴇᴍʙᴇʀs ʜᴀᴠᴇ ᴛᴏ sᴜʙsᴄʀɪʙᴇ ᴛʜɪs [ᴄʜᴀɴɴᴇʟ](https://t.me/{input_str}) ғᴏʀ sᴇɴᴅɪɴɢ ᴍᴇssᴀɢᴇs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.__",
                        disable_web_page_preview=True,
                    )
                except UserNotParticipant:
                    message.reply_text(
                        f"😕 **ɪ'ᴍ ɴᴏᴛ ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ**\n__ᴩʀᴏᴍᴏᴛᴇ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴇ [ᴄʜᴀɴɴᴇʟ](https://t.me/{input_str}) ᴛᴏ ᴇɴᴀʙʟᴇ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ.__",
                        disable_web_page_preview=True,
                    )
                except (UsernameNotOccupied, PeerIdInvalid):
                    message.reply_text(f"**» ɪɴᴠᴀʟɪᴅ ᴄʜᴀɴɴᴇʟ ᴜsᴇʀɴᴀᴍᴇ.**")
                except Exception as err:
                    message.reply_text(f"**ᴇʀʀᴏʀ:** ```{err}```")
        else:
            if sql.fs_settings(chat_id):
                message.reply_text(
                    f"**» ғᴏʀᴄᴇ sᴜʙ ɪs ᴇɴᴀʙʟᴇᴅ.**\n__ғᴏʀ ᴛʜɪs [ᴄʜᴀɴɴᴇʟ](https://t.me/{sql.fs_settings(chat_id).channel})__",
                    disable_web_page_preview=True,
                )
            else:
                message.reply_text("**» ғᴏʀᴄᴇ sᴜʙ ɪs ᴅɪsᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.**")
    else:
        message.reply_text(
            "**» ᴏɴʟʏ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜɪs ᴄʜᴀᴛ ᴄᴀɴ ᴇɴᴀʙʟᴇ ғᴏʀᴄᴇ sᴜʙsᴄʀɪʙᴇ.**"
        )


__help__ = """
  *Force Subscribe:*

  Fallen Robot can mute members who are not subscribed your channel until they subscribe When enabled I will mute unsubscribed members and show them a unmute button. When they pressed the button I will unmute them

  *Setup* *:* *Only for chat owner*
  ❍ Add me in your group as admin
  ❍ Add me in your channel as admin 
    
  *Commmands*
  ❍ /fsub {channel username} *:* To turn on and setup the channel.

    💡Do this first...

  ❍ /fsub *:* To get the current settings.
  ❍ /fsub disable *:* To turn of ForceSubscribe..

    💡If you disable fsub, you need to set again for working.. /fsub {channel username} 

  ❍ /fsub clear *:* To unmute all members who are muted by me for not joining the channel.
"""
__mod_name__ = "Fᴏʀᴄᴇ-Sᴜʙ"
