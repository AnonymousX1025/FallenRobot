from geopy.geocoders import Nominatim
from telethon import *
from telethon.tl import *

from FallenRobot import *
from FallenRobot import telethn as tbot
from FallenRobot.events import register

GMAPS_LOC = "https://maps.googleapis.com/maps/api/geocode/json"


@register(pattern="^/gps (.*)")
async def _(event):
    args = event.pattern_match.group(1)

    try:
        geolocator = Nominatim(user_agent="SkittBot")
        location = args
        geoloc = geolocator.geocode(location)
        longitude = geoloc.longitude
        latitude = geoloc.latitude
        gm = "https://www.google.com/maps/search/{},{}".format(latitude, longitude)
        await tbot.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(latitude), float(longitude))
            ),
        )
        await event.reply(
            "ᴏᴘᴇɴ ᴡɪᴛʜ: [🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘs]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")


__help__ = """
sᴇɴᴅs ʏᴏᴜ ᴛʜᴇ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ...

 ❍ /gps <ʟᴏᴄᴀᴛɪᴏɴ>*:* ɢᴇᴛ ɢᴘs ʟᴏᴄᴀᴛɪᴏɴ.
"""

__mod_name__ = "Gᴘs"
