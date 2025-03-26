import threading

from sqlalchemy import Column, String

from SagiriRobot.modules.sql import BASE, SESSION


class SagiriChats(BASE):
    __tablename__ = "dazai_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


SagiriChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_sagiri(chat_id):
    try:
        chat = SESSION.query(SagiriChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_sagiri(chat_id):
    with INSERTION_LOCK:
        sagirichat = SESSION.query(SagiriChats).get(str(chat_id))
        if not sagirichat:
            sagirichat = SagiriChats(str(chat_id))
        SESSION.add(sagarichat)
        SESSION.commit()


def rem_sagiri(chat_id):
    with INSERTION_LOCK:
        sagirichat = SESSION.query(SagiriChats).get(str(chat_id))
        if sagirichat:
            SESSION.delete(sagirichat)
        SESSION.commit()
