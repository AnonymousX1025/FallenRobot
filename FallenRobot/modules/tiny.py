import os
import cv2
from PIL import Image
from FallenRobot.events import register
from FallenRobot import telethn as tbot


@register(pattern="^/tiny ?(.*)")
async def _(event):
    reply = await event.get_reply_message()
    if not (reply and(reply.media)):
           await event.reply("`Please reply to a sticker`")
           return
    kontol = await event.reply("`Processing tiny...`")
    ik = await tbot.download_media(reply)
    im1 = Image.open("FallenRobot/resources/blank_background.png")
    if ik.endswith(".tgs"):
        await tbot.download_media(reply, "blank_background.tgs")
        os.system("lottie_convert.py blank_background.tgs json.json")
        json = open("json.json", "r")
        jsn = json.read()
        jsn = jsn.replace("512", "2000")
        open = ("json.json", "w").write(jsn)
        os.system("lottie_convert.py json.json blank_background.tgs")
        file = "blank_background.tgs"
        os.remove("json.json")
    elif ik.endswith((".gif", ".mp4")):
        iik = cv2.VideoCapture(ik)
        busy = iik.read()
        cv2.imwrite("i.png", busy)
        fil = "i.png"
        im = Image.open(fil)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove(fil)
        os.remove("k.png")
    else:
        im = Image.open(ik)
        z, d = im.size
        if z == d:
            xxx, yyy = 200, 200
        else:
            t = z + d
            a = z / t
            b = d / t
            aa = (a * 100) - 50
            bb = (b * 100) - 50
            xxx = 200 + 5 * aa
            yyy = 200 + 5 * bb
        k = im.resize((int(xxx), int(yyy)))
        k.save("k.png", format="PNG", optimize=True)
        im2 = Image.open("k.png")
        back_im = im1.copy()
        back_im.paste(im2, (150, 0))
        back_im.save("o.webp", "WEBP", quality=95)
        file = "o.webp"
        os.remove("k.png")
    await tbot.send_file(event.chat_id, file, reply_to=event.reply_to_msg_id)
    await kontol.delete()
    os.remove(file)
    os.remove(ik)
__mod_name__ = "Tɪɴʏ"
__help__ = """
❍ /tiny*:* reply a sticker and see magic
"""
