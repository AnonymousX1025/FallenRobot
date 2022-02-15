from FallenRobot import telethn
from FallenRobot.events import register

@register(pattern="^/hi$")
async def _(event):
    j = "Bol na lavde"
    await event.reply(j)
    
__mod_name__ = "Hi"
