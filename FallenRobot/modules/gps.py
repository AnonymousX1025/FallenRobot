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
        geolocator = Nominatim(user_agent="FallenRobot")
        geoloc = geolocator.geocode(args)
        gm = f"https://www.google.com/maps/search/{geoloc.latitude},{geoloc.longitude}"
        await tbot.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(
                types.InputGeoPoint(float(geoloc.latitude), float(geoloc.longitude))
            ),
        )
        await event.reply(
            f"ᴏᴘᴇɴ ᴡɪᴛʜ : [🌏ɢᴏᴏɢʟᴇ ᴍᴀᴘs]({gm})",
            link_preview=False,
        )
    except:
        await event.reply("I can't find that")


__help__ = """
Sends you the gps location of the given query...

 ❍ /gps <location> *:* Get gps location.
"""

__mod_name__ = "Gᴘs"
