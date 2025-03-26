from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from SagiriRobot import OWNER_ID as owner_id
from SagiriRobot import SUPPORT_CHAT as log,BOT_NAME,START_IMG
from SagiriRobot import pbot as Client
from SagiriRobot.utils.errors import capture_err


def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
@capture_err
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = f"@{msg.chat.username}/`{msg.chat.id}`"
    else:
        chat_username = f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{msg.chat.id}`"

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = (
        "[" + msg.from_user.first_name + "](tg://user?id=" + str(msg.from_user.id) + ")"
    )
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    

    bug_report = f"""
**#𝙽ᴇᴡʙᴜɢ : ** **tg://user?id={owner_id}**

**⨬ 𝚁ᴇᴩᴏʀᴛᴇᴅ ʙʏ : ** **{mention}**
**⌯ 𝚄sᴇʀ ɪᴅ : ** **{user_id}**
**⎋ 𝙲ʜᴀᴛ ɢʀᴏᴜᴘ : ** **{chat_username}**

**⚠️B̸ᴜɢ : ** **{bugs}**

**➱𝙴ᴠᴇɴᴛ sᴛᴀᴍᴩ : ** **{datetimes}**"""

    if msg.chat.type == "private":
        await msg.reply_text("<b>» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴩs.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>» ᴀʀᴇ ʏᴏᴜ ᴄᴏᴍᴇᴅʏ ᴍᴇ 🤣, ʏᴏᴜ'ʀᴇ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ʙᴏᴛ.</b>",
            )
            return
        else:
            await msg.reply_text("ᴄʜᴜᴍᴛɪʏᴀ ᴏᴡɴᴇʀ!")
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>⎆𝙽ᴇᴡ ʙᴜɢ ʀᴇᴩᴏʀᴛ : {bugs}</b>\n\n"
                "<b>⟳ 𝚃𝙷𝙸𝚂 𝙱𝚄𝙶 𝙷𝙰𝚂 𝙱𝙴𝙴𝙽 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝚁𝙴𝙿𝙾𝚁𝚃𝙴𝙳 𝙰𝚃 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃 !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url=f"https://t.me/Gojo_support_chat")]]
                ),
            )
            await Client.send_photo(
                log,
                photo=START_IMG,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("ᴠɪᴇᴡ ʙᴜɢ", url=f"{msg.link}")],
                        [
                            InlineKeyboardButton(
                                "ᴄʟᴏsᴇ", callback_data="close_send_photo"
                            )
                        ],
                    ]
                ),
            )
        else:
            await msg.reply_text(
                f"<b>» ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴩᴏʀᴛ !</b>",
            )


@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()


@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_, CallbackQuery):
    is_Admin = await Client.get_chat_member(
        CallbackQuery.message.chat.id, CallbackQuery.from_user.id
    )
    if not is_Admin.can_delete_messages:
        return await CallbackQuery.answer(
            "𝙾𝙿𝙿𝚂 𝙱𝚁𝚄𝚅 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝚁𝙸𝙶𝙷𝚃𝚂 𝚃𝙾 𝙲𝙻𝙾𝚂𝙴.", show_alert=True
        )
    else:
        await CallbackQuery.message.delete()


__help__ = """
*𝙵ᴏʀ ʀᴇᴩᴏʀᴛɪɴɢ ᴀ ʙᴜɢ *
 ❍ /bug *:* 𝚃ᴏ ʀᴇᴩᴏʀᴛ ᴀ ʙᴜɢ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ.
"""
__mod_name__ = "Bᴜɢꜱ"
