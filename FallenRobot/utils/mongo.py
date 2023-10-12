from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from FallenRobot import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
db = mongo.FallenRobot

coupledb = db.couple
tokendb = db.tokens


async def _get_lovers(chat_id: int):
    lovers = await coupledb.find_one({"chat_id": chat_id})
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
    await coupledb.update_one(
        {"chat_id": chat_id},
        {"$set": {"couple": lovers}},
        upsert=True,
    )


async def is_user(user_id: int) -> bool:
    user = await tokendb.find_one({"user_id": user_id})
    if user:
        return user["api"]
    else:
        return False

async def add_user(user_id: int, api: str):
    user = await is_user(user_id)
    if not user:
        return await tokendb.insert_one({"user_id": user_id, "api": api})

async def remove_user(user_id: int, api: str):
    user = await is_user(user_id)
    if not user:
        return
    return await tokendb.delete_one({"user_id": user_id, "api": api})
