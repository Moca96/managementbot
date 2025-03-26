import html
import asyncio
from pyrogram import *
from pyrogram.raw.types import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from SagiriRobot import pbot as pgram
from pyrogram import filters

import logging

                

@pgram.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇꜱꜱᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if not message.command:
        message.command = message.text.split()
        
    if not message.command:
        message.command = message.text.split()

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[𝚄𝚂𝙴𝚁 𝙸𝙳:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("This user doesn't exist.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if not getattr(reply, "empty", True) and not message.forward_from_chat and not reply.sender_chat:
        text += (
            f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ɪᴅ:]({reply.link})** `{message.reply_to_message.id}`\n"
        )
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜꜱᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"The forwarded channel, {reply.forward_from_chat.title}, has an id of `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)
    
    if reply and reply.sender_chat:
        text += f"ID of the replied chat/channel, is `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
       text,
       disable_web_page_preview=True,
   )   
