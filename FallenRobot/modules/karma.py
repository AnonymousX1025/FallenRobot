import asyncio 
import re

from pyrogram import filters

from FallenRobot import pbot as pgram
from FallenRobot.utils.errors import capture_err
from FallenRobot.modules.helper_funcs.chat_status import user_admin
from FallenRobot.helper_extra.dbfun import (alpha_to_int, get_karma,
                                   get_karmas, int_to_alpha, update_karma)   
from FallenRobot.helper_extra.dbfun import is_karma_on, karma_off, karma_on

karma_positive_group = 3
karma_negative_group = 4

regex_upvote = r"^((?i)\+|\+\+|\+1|thx|tnx|ty|thank you|thanx|thanks|pro|cool|good|👍)$"
regex_downvote = r"^(\-|\-\-|\-1|👎)$"

@pgram.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_upvote, re.IGNORECASE)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_positive_group,
)
@capture_err
async def upvote(_, message):
    if not await is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return
    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(
        chat_id, await int_to_alpha(user_id)
    )
    if current_karma:
        current_karma = current_karma['karma']
        karma = current_karma + 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(
        chat_id, await int_to_alpha(user_id), new_karma
    )
    await message.reply_text(
        f"Incremented Karma of {user_mention} By 1 \nTotal Points: {karma}"
    )


@pgram.on_message(
    filters.text
    & filters.group
    & filters.incoming
    & filters.reply
    & filters.regex(regex_downvote, re.IGNORECASE)
    & ~filters.via_bot
    & ~filters.bot
    & ~filters.edited,
    group=karma_negative_group,
)
@capture_err
async def downvote(_, message):
    if not await is_karma_on(message.chat.id):
        return
    if not message.reply_to_message.from_user:
        return
    if not message.from_user:
        return
    if message.reply_to_message.from_user.id == message.from_user.id:
        return

    chat_id = message.chat.id
    user_id = message.reply_to_message.from_user.id
    user_mention = message.reply_to_message.from_user.mention
    current_karma = await get_karma(
        chat_id, await int_to_alpha(user_id)
    )
    if current_karma:
        current_karma = current_karma['karma']
        karma = current_karma - 1
    else:
        karma = 1
    new_karma = {"karma": karma}
    await update_karma(
        chat_id, await int_to_alpha(user_id), new_karma
    )
    await message.reply_text(
        f"Decremented Karma Of {user_mention} By 1 \nTotal Points: {karma}"
    )


@pgram.on_message(filters.command("karma") & filters.group)
@capture_err
async def command_karma(_, message):
    chat_id = message.chat.id
    if not message.reply_to_message:
        m = await message.reply_text(
            "Getting Karma list of top 10 users wait..."
        )
        karma = await get_karmas(chat_id)
        if not karma:
            await m.edit("No karma in DB for this chat.")
            return
        msg = f"🏆 Top list of Karma owners in the {message.chat.title}»: \n"
        limit = 0
        karma_dicc = {}
        for i in karma:
            user_id = await alpha_to_int(i)
            user_karma = karma[i]['karma']
            karma_dicc[str(user_id)] = user_karma
            karma_arranged = dict(
                sorted(
                    karma_dicc.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            )
        if not karma_dicc:
            await m.edit("No karma in DB for this chat.")
            return
        for user_idd, karma_count in karma_arranged.items():
            if limit > 9:
                break
            try:
                user = await pgram.get_users(int(user_idd))
                await asyncio.sleep(0.8)
            except Exception:
                continue
            first_name = user.first_name
            if not first_name:
                continue
            username = user.username
            msg += f"\n[{first_name}](https://t.me/{username}) — {karma_count}"
            limit += 1
        await m.edit(msg, disable_web_page_preview=True)
    else:
        user_id = message.reply_to_message.from_user.id
        karma = await get_karma(chat_id, await int_to_alpha(user_id))
        karma = karma['karma'] if karma else 0
        await message.reply_text(f"**Total Points**: __{karma}__")


@user_admin
@pgram.on_message(filters.command("karmas") & ~filters.private)
async def captcha_state(_, message):
    usage = "**Usage:**\n/karmas [on|off]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        await karma_on(chat_id)
        await message.reply_text("Enabled karma System!")
    elif state == "off":
        await karma_off(chat_id)
        await message.reply_text("Disabled karma System!")
    else:
        await message.reply_text(usage)

__mod_name__ = "Kᴀʀᴍᴀ"
__help__ = """
*Upvote* - Use upvote keywords like "+", "+1", "thanks", etc. to upvote a message.
*Downvote* - Use downvote keywords like "-", "-1", etc. to downvote a message.
*Commands*
•/karma:- reply to a user to check that user's karma points.
•/karma:- send without replying to any message to check karma point list of top 10
•/karmas [off/on] :- Enable/Disable karma in your group.
"""
