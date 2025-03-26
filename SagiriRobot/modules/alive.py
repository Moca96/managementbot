#by @jashxn_69 pvt.

import asyncio
import random
from sys import version_info

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from AnonyxJashan.helper import PHOTO
from SagiriRobot import BOT_NAME
from SagiriRobot import BOT_USERNAME as fuck
from SagiriRobot import pbot as pgram

ASAU = [
    [
        InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇꜱ", url=f"https://t.me/yamada_updates"),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/yamada_test"),
    ],  
]


@pgram.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    yamada = await m.reply("⚡")
    await asyncio.sleep(1)
    await yamada.edit("𝐀ʟɪᴠɪɴɢ.")
    await asyncio.sleep(0.1)
    await yamada.edit("𝐆ᴇᴛᴛɪɴɢ ɪɴꜰᴏ..")
    await asyncio.sleep(0.1)
    await yamada.edit("𝐆ᴇᴛᴛɪɴɢ ɪɴꜰᴏ...")
    await yamada.delete()
    await asyncio.sleep(0.1)
    jashan = await m.reply_sticker(
        "CAACAgUAAxkBAAIEzWS3rFkKqNjyWYxjQU5PUvaI_okcAAKKCQAC71yIVfrJ5_5sNT_GLwQ"
    )
    await asyncio.sleep(0.1)
    await m.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
     ▱▱▱▱▱▱▱▱▱▱▱▱
⟐ **ᴍʏ ᴏᴡɴᴇʀ :** [𝙶ᴏᴊᴏ ꜱᴀᴛᴏʀᴜ](https://t.me/Gojo_Satoru_botx)
⟐ **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{lver}`
⟐ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{tver}`
⟐ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
⟐ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
◎ **ʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `1.0`
     ▱▱▱▱▱▱▱▱▱▱▱▱""",
        reply_markup=InlineKeyboardMarkup(ASAU),
    )
