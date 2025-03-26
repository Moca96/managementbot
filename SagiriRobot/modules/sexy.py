#by @jashxn_69 

import random, requests, time

from telethon import Button, events

from SagiriRobot import telethn as asst
from pyrogram import filters
from pyrogram.types import *
from SagiriRobot.events import register
from SagiriRobot import pbot as bot

@bot.on_message(filters.command("wish"))
async def wish(_, m):
            if len(m.command) <  2:
                  await m.reply("🍒 ~~**Aᴅᴅ~~ ᴡɪꜱʜ!**")
                  return 
            api = requests.get("https://nekos.best/api/v2/happy").json()
            url = api["results"][0]['url']
            text = m.text.split(None, 1)[1]
            wish_count = random.randint(1,100)
            wish = f"❄️ **Hᴇʏ! {m.from_user.first_name}!** \n"
            wish += f"✨ **ʏᴏᴜʀ ᴡɪꜱʜ :** {text} \n"
            wish += f"🫧 **ᴘᴏꜱꜱɪʙʟᴇ ᴛᴏ :** {wish_count}%"
            await m.reply_animation(url,caption=(wish),
              reply_markup=InlineKeyboardMarkup(
                    [ [InlineKeyboardButton("𝙶ᴏᴊᴏ 𝚂ᴀᴛᴏʀᴜ  🧃", url=f"https://t.me/Gojo_Satoru_botx")]]))
            

BUTTON = [[Button.url("𝙶ᴏᴊᴏ 𝚂ᴀᴛᴏʀᴜ 🧃", "https://t.me/Gojo_Satoru_botx")]]
HOT = "https://telegra.ph/file/f7687f927cbd8d84568e0.mp4"
SMEXY = "https://te.legra.ph/file/560eaae8954adc098aacf.mp4"
LEZBIAN = "https://telegra.ph/file/6f9a98b5a4629db33dd21.mp4"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANG = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://telegra.ph/file/b0c9132841643c6c9119a.mp4"
SIG = "https://telegra.ph/file/2c1190751777576cedbb9.mp4"
BAT = "https://telegra.ph/file/a5b0781ebe5b3d6988f85.mp4"
GIGA = "https://te.legra.ph/file/9dffcc8499681b3023a30.mp4"
PSYCHOPATH = "https://te.legra.ph/file/fd6c10493d2a277c2c5c1.mp4"

@asst.on(events.NewMessage(pattern="/horny ?(.*)"))
async def horny(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    HORNY = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ!**"
    await e.reply(HORNY, buttons=BUTTON, file=HOT)


@asst.on(events.NewMessage(pattern="/gay ?(.*)"))
async def gay(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    GAY = f"**🏳‍🌈** {mention} **ɪꜱ** {mm}**% ɢᴀʏ!**"
    await e.reply(GAY, buttons=BUTTON, file=SMEXY)


@asst.on(events.NewMessage(pattern="/lesbian ?(.*)"))
async def leꜱbian(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    LESBIAN = f"**🏳‍🌈** {mention} **ɪꜱ** {mm}**% ʟᴇꜱʙɪᴀɴ!**"
    await e.reply(LESBIAN, buttons=BUTTON, file=LEZBIAN)


@asst.on(events.NewMessage(pattern="/boob ?(.*)"))
async def boob(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BOOBS = f"**🍒** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}**!**"
    await e.reply(BOOBS, buttons=BUTTON, file=BIGBALL)


@asst.on(events.NewMessage(pattern="/cock ?(.*)"))
async def cock(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    COCK = f"**🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ**"
    await e.reply(COCK, buttons=BUTTON, file=LANG)


@asst.on(events.NewMessage(pattern="/cute ?(.*)"))
async def cute(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CUTE = f"**🍑** {mention} {mm}**% ᴄᴜᴛᴇ**"
    await e.reply(CUTE, buttons=BUTTON, file=CUTIE)


@asst.on(events.NewMessage(pattern="/sigma ?(.*)"))
async def sigma(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    SIGMA = f"**🗿** {mention} **ɪꜱ** {mm}**% ꜱɪɢᴍᴀ!**"
    await e.reply(SIGMA, buttons=BUTTON, file=SIG)


@asst.on(events.NewMessage(pattern="/batman ?(.*)"))
async def batman(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    BATMAN = f"**🦇** {mention} **ɪꜱ** {mm}**% ʙᴀᴛᴍᴀɴ!**"
    await e.reply(BATMAN, buttons=BUTTON, file=BAT)


@asst.on(events.NewMessage(pattern="/chad ?(.*)"))
async def chad(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    CHAD = f"**🗿** {mention} **ɪꜱ** {mm}**% ɢɪɢᴀ-ᴄʜᴀᴅ!**"
    await e.reply(CHAD, buttons=BUTTON, file=GIGA)
            

@asst.on(events.NewMessage(pattern="/psycho ?(.*)"))
async def psycho(e):
    user_id = e.sender.id
    user_name = e.sender.first_name
    mention = f"[{user_name}](tg://user?id={str(user_id)})"
    mm = random.randint(1, 100)
    PSYCHO = f"**😈** {mention} **ɪꜱ** {mm}**% ᴘꜱʏᴄʜᴏ!**"
    await e.reply(PSYCHO, buttons=BUTTON, file=PSYCHOPATH)


__help__ = """
➱ /horny - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʜᴏʀɴʏᴇꜱꜱ

➱/wish - ɢᴇᴛ ꜱᴏᴍᴇ ᴡɪɪꜱʜᴇꜱ ᴀɴᴅ ꜱᴇᴇ ʜᴏᴡ ᴍᴀɴʏ ᴘᴏꜱꜱɪʙɪʟᴛʏ ᴏꜰ ʏᴏᴜʀ ᴡɪꜱʜ  ᴀʀᴇ ᴛᴜʀᴇ

➱ /gay - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ɢᴜʏɴᴇꜱꜱ

➱ /lezbian - ᴄʜᴇᴄᴋ ᴜʀ ᴄᴜʀʀᴇɴᴛ ʟᴀᴢʙɪᴀɴ

➱ /boob - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ʙᴏᴏʙꜱ ꜱɪᴢᴇ

➱ /cute - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ᴄᴜᴛᴇɴᴇꜱꜱ

➱ /sigma - ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴄᴜʀʀᴇɴᴛ ꜱɪɢᴍᴀɴᴇꜱ

➱ /batman - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴜᴄʜ ɢᴏᴛʜᴀᴍ ɴᴇᴇᴅꜱ ʏᴏᴜ

➱ /chad - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴜᴄʜ ɢɪɢᴀ ᴄʜᴀᴅ ʏᴏᴜ'ʀᴇ

➱ /chad - ᴄʜᴇᴄᴋ ʜᴏᴡ ᴍᴜᴄʜ ᴘꜱʏᴄʜᴏ ʏᴏᴜ'ʀᴇ
"""

__mod_name__ = "Hᴏʀɴʏ-ɢᴀᴍᴇꜱ"
