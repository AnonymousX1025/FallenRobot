from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hᴇʏ {},

Wᴇʟᴄᴏᴍᴇ ᴛᴏ {}

Iғ ʏᴏᴜ ᴅɪᴅɴ'ᴛ ᴛʀᴜsᴛ ᴛʜɪs ʙᴏᴛ,
𝟷. Sᴛᴏᴘ ʀᴇᴀᴅɪɴɢ ᴛʜɪs ᴍᴇssᴀɢᴇ.
𝟸. Dᴇʟᴇᴛᴇ ᴛʜɪs ᴄʜᴀᴛ.

I ᴋɴᴏᴡ ʏᴏᴜ ᴀʀᴇ sᴛɪʟʟ ʀᴇᴀᴅɪɴɢ,
Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ Pʏʀᴏɢʀᴀᴍ ᴀɴᴅ Tᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ. Usᴇ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ !

ʙʏ [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](t.me/anonymous_was_bot)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")]
    ]

    # Help Message
    HELP = """
✨ **ᴍʏ ᴄᴏᴍᴍᴀɴᴅs** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Start Generating Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴍᴇ** 

A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ @AnonymousRobotSupport

ꜰʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](t.me/anonymous_was_bot)
    """
