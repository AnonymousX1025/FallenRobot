from aiohttp import ClientSession


async def post(url: str, *args, **kwargs):
    async with ClientSession().post(url, *args, **kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data
