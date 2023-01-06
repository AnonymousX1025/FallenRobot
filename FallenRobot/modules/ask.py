import os

import openai
from gtts import gTTS
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from FallenRobot import AI_KEY, BOT_NAME, OWNER_ID, pbot

openai.api_key = AI_KEY
completion = openai.Completion()
qr = {}


def get_resp(ques):
    something = f"Anonymous: {ques}\n {BOT_NAME}: "
    resp = completion.create(
        prompt=something,
        engine="text-davinci-003",
        max_tokens=256,
        stop=["\Anonymous"],
    )
    answer = resp.choices[0].text.strip()
    return answer


@pbot.on_message(filters.command(["ask", "tell"]))
async def results(_, message: Message):
    ques = message.text.split(None, 1)[1]
    if "who is your owner" in ques.lower():
        return await message.reply_text(
            f"My owner is [Prakhar](tg://openmessage?user_id={OWNER_ID})",
            disable_web_page_preview=True,
        )
    elif "who is your creator" in ques.lower():
        return await message.reply_text(
            f"I was created by [Prakhar](tg://openmessage?user_id={OWNER_ID})",
            disable_web_page_preview=True,
        )
    response = get_resp(ques)
    cd = str(message.id) + "|" + str(0) + "|" + str(0)
    qr[message.id] = [[], []]
    await message.reply_text(
        text=response,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="👍🏻", callback_data=f"upthumb {cd}"),
                    InlineKeyboardButton(text="👎🏻", callback_data=f"downthumb {cd}"),
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@pbot.on_message(filters.command(["asks"]))
async def v_results(_, message: Message):
    ques = message.text.split(None, 1)[1]
    if "who is your owner" in ques.lower():
        response = f"My owner is Prakhar"
    elif "who is your creator" in ques.lower():
        response = f"I was created by Prakhar"
    else:
        response = get_resp(ques)
    tts = gTTS(response, lang="en")
    fname = "audio.mp3"
    tts.save(fname)
    await pbot.send_voice(
        chat_id=message.chat.id,
        voice=fname,
        reply_to_message_id=message.id,
        protect_content=True,
    )
    try:
        os.remove(fname)
    except:
        pass
