from io import BytesIO

from aiohttp import ClientSession


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with ClientSession().post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image
