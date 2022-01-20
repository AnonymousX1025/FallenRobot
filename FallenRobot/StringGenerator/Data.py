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

ʙʏ [𝗗𝝣∇𝗜𝗟'𝗦 𝗛𝝣𝝙∇𝝣𝗡](t.me/DevilsHeavenMF)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 ʀᴇᴛᴜʀɴ ʜᴏᴍᴇ 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ sᴛʀɪɴɢ 🔥", callback_data="generate")],
        [
            InlineKeyboardButton("ʜᴇʟᴘ ❔", callback_data="help"),
            InlineKeyboardButton("🎪 ᴀʙᴏᴜᴛ 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/DevilsHeavenMF")],
  ]

    # Help Message
    HELP = """
✨ **ᴍʏ ᴄᴏᴍᴍᴀɴᴅs** ✨

» /about : About The Bot
» /generate : Start Generating Session
» /cancel : Cancel the process
"""

    # About Message
    ABOUT = """
**ᴀʙᴏᴜᴛ ᴍᴇ** 

A ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ ᴀɴᴅ ᴛᴇʟᴇᴛʜᴏɴ sᴛʀɪɴɢ sᴇssɪᴏɴ ʙʏ [𝗗𝝣∇𝗜𝗟'𝗦 𝗛𝝣𝝙∇𝝣𝗡](t.me/DevilsHeavenMF)

ꜰʀᴀᴍᴇᴡᴏʀᴋ : [Pyrogram](docs.pyrogram.org)

ʟᴀɴɢᴜᴀɢᴇ : [Python](www.python.org)

ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝝙𝗡𝗢𝗡𝗬𝗠𝗢𝗨𝗦](t.me/anonymous_was_bot)
    """
