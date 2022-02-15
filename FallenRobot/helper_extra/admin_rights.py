import asyncio

from telegram import User, Chat


def user_can_promote(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_promote_members


def user_can_ban(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_restrict_members


def user_can_pin(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_pin_messages


def user_can_changeinfo(chat: Chat, user: User, bot_id: int) -> bool:
    return chat.get_member(user.id).can_change_info

async def is_admin(event, user):
    try:
        sed = await event.client.get_permissions(event.chat_id, user)
        is_mod = bool(sed.is_admin)
    except:
        is_mod = False
    return is_mod
