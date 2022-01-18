from FallenRobot import MONGO_DB_URI
from typing import Dict, List, Union
from pymongo import MongoClient

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["FallenRobot"]

coupledb = db.couple
karmadb = db.karma





async def _get_lovers(chat_id: int):
    lovers = coupledb.find_one({"chat_id": chat_id})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers


async def get_couple(chat_id: int, date: str):
    lovers = await _get_lovers(chat_id)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(chat_id: int, date: str, couple: dict):
    lovers = await _get_lovers(chat_id)
    lovers[date] = couple
    coupledb.update_one({"chat_id": chat_id}, {"$set": {"couple": lovers}}, upsert=True)





async def get_karmas_count() -> dict:
    chats = karmadb.find({"chat_id": {"$lt": 0}})
    if not chats:
        return {}
    chats_count = 0
    karmas_count = 0
    for chat in await chats.to_list(length=1000000):
        for i in chat["karma"]:
            karmas_count += chat["karma"][i]["karma"]
        chats_count += 1
    return {"chats_count": chats_count, "karmas_count": karmas_count}


async def get_karmas(chat_id: int) -> Dict[str, int]:
    karma = karmadb.find_one({"chat_id": chat_id})
    if karma:
        karma = karma["karma"]
    else:
        karma = {}
    return karma


async def get_karma(chat_id: int, name: str) -> Union[bool, dict]:
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    if name in karmas:
        return karmas[name]


async def update_karma(chat_id: int, name: str, karma: dict):
    name = name.lower().strip()
    karmas = await get_karmas(chat_id)
    karmas[name] = karma
    karmadb.update_one({"chat_id": chat_id}, {"$set": {"karma": karmas}}, upsert=True)





async def int_to_alpha(user_id: int) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    text = ""
    user_id = str(user_id)
    for i in user_id:
        text += alphabet[int(i)]
    return text


async def alpha_to_int(user_id_alphabet: str) -> int:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    user_id = ""
    for i in user_id_alphabet:
        index = alphabet.index(i)
        user_id += str(index)
    user_id = int(user_id)
    return user_id
