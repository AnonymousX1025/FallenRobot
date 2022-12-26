import threading

from sqlalchemy import Column, String

from FallenRobot.modules.sql import BASE, SESSION


class FallenChats(BASE):
    __tablename__ = "fallen_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


FallenChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_fallen(chat_id):
    try:
        chat = SESSION.query(FallenChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_fallen(chat_id):
    with INSERTION_LOCK:
        fallenchat = SESSION.query(FallenChats).get(str(chat_id))
        if not fallenchat:
            fallenchat = FallenChats(str(chat_id))
        SESSION.add(fallenchat)
        SESSION.commit()


def rem_fallen(chat_id):
    with INSERTION_LOCK:
        fallenchat = SESSION.query(FallenChats).get(str(chat_id))
        if fallenchat:
            SESSION.delete(fallenchat)
        SESSION.commit()
