import os
from FallenRobot import telethn as tbot
from geopy.geocoders import Nominatim
from FallenRobot.events import register
from FallenRobot import *
from telethon import *
from telethon.tl import *

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
            "Open with: [🌏Google Maps]({})".format(gm),
            link_preview=False,
        )
    except Exception as e:
        print(e)
        await event.reply("I can't find that")


__help__ = """
Sends you the gps location of the given query...

 ❍ /gps <location>*:* Get gps location.
"""

__mod_name__ = "Gᴘs"
