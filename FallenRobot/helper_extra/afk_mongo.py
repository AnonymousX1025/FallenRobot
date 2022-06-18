from FallenRobot.helper_extra.dbfun import db

usersdb = db.users


async def is_afk(user_id: int) -> bool:
    user = usersdb.find_one({"user_id": user_id})
    if not user:
        return False, {}
    return True, user["reason"]


async def add_afk(user_id: int, mode):
    usersdb.update_one(
        {"user_id": user_id}, {"$set": {"reason": mode}}, upsert=True
    )


async def remove_afk(user_id: int):
    user = usersdb.find_one({"user_id": user_id})
    if user:
        return usersdb.delete_one({"user_id": user_id})


async def get_afk_users() -> list:
    users = usersdb.find({"user_id": {"$gt": 0}})
    if not users:
        return []
    users_list = []
    for user in users.to_list(length=1000000000):
        users_list.append(user)
    return users_list
