from SagiriRobot import pbot as pgram, BOT_USERNAME
from pyrogram import filters
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton
)

whisper_db = {}

switch_btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔐 𝚂ᴛᴀʀᴛ ᴡʜɪꜱᴘᴇʀ", switch_inline_query_current_chat="")]])

async def _whisper(_, inline_query):
    data = inline_query.query
    results = []
    
    if len(data.split()) < 2:
        mm = [
            InlineQueryResultArticle(
                title="🔐 𝚆ʜɪꜱᴘᴇʀ",
                description=f"@{BOT_USERNAME} [ USERNAME | ID ] [ TEXT ]",
                input_message_content=InputTextMessageContent(f"🧃 𝚄ꜱᴀɢᴇ:\n\n@{BOT_USERNAME} [ USERNAME | ID ] [ TEXT ]"),
                thumb_url="https://telegra.ph/file/5406ed880a8089c6add3b.jpg",
                reply_markup=switch_btn
            )
        ]
    else:
        try:
            user_id = data.split()[0]
            msg = data.split(None, 1)[1]
        except IndexError as e:
            pass
        
        try:
            user = await _.get_users(user_id)
        except:
            mm = [
                InlineQueryResultArticle(
                    title="🔐 𝚆ʜɪꜱᴘᴇʀ",
                    description="Invalid username or ID!",
                    input_message_content=InputTextMessageContent("Invalid username or ID!"),
                    thumb_url="https://telegra.ph/file/5406ed880a8089c6add3b.jpg",
                    reply_markup=switch_btn
                )
            ]
        
        try:
            whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("🔐 𝚆ʜɪꜱᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}")]])
            one_time_whisper_btn = InlineKeyboardMarkup([[InlineKeyboardButton("📬 𝙾ɴᴇ-ᴛɪᴍᴇ ᴡʜɪꜱᴘᴇʀ", callback_data=f"fdaywhisper_{inline_query.from_user.id}_{user.id}_one")]])
            mm = [
                InlineQueryResultArticle(
                    title="🔐 𝚆ʜɪꜱᴘᴇʀ",
                    description=f"𝚂ᴇɴᴅ ᴀ ᴡʜɪꜱᴘᴇʀ ᴛᴏ {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"🔐 𝚈ᴏᴜ'ʀᴇ ꜱᴇɴᴅɪɴɢ ᴀ ᴡʜɪꜱᴘᴇʀ ᴛᴏ {user.first_name}.\n\nType your message/sentence."),
                    thumb_url="https://telegra.ph/file/5406ed880a8089c6add3b.jpg",
                    reply_markup=whisper_btn
                ),
                InlineQueryResultArticle(
                    title="📬 𝙾ɴᴇ-ᴛɪᴍᴇ ᴡʜɪꜱᴘᴇʀ",
                    description=f"𝚂ᴇɴᴅ ᴀ ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪꜱᴘᴇʀ ᴛᴏ {user.first_name}!",
                    input_message_content=InputTextMessageContent(f"📬 ʏᴏᴜ'ʀᴇ ꜱᴇɴᴅɪɴɢ ᴀ ᴏɴᴇ-ᴛɪᴍᴇ ᴡʜɪꜱᴘᴇʀ ᴛᴏ {user.first_name}.\n\nType your message/sentence."),
                    thumb_url="https://telegra.ph/file/5406ed880a8089c6add3b.jpg",
                    reply_markup=one_time_whisper_btn
                )
            ]
        except:
            pass
        
        try:
            whisper_db[f"{inline_query.from_user.id}_{user.id}"] = msg
        except:
            pass
    
    results.append(mm)
    return results


@pgram.on_callback_query(filters.regex(pattern=r"fdaywhisper_(.*)"))
async def whispes_cb(_, query):
    data = query.data.split("_")
    from_user = int(data[1])
    to_user = int(data[2])
    user_id = query.from_user.id
    
    if user_id not in [from_user, to_user, 5667156680]:
        try:
            await _.send_message(from_user, f"{query.from_user.mention} ɪꜱ ᴛʀʏɪɴɢ ᴛᴏ ᴏᴘᴇɴ ʏᴏᴜʀ ᴡʜɪꜱᴘᴇʀ. ᴘʟᴇᴀꜱᴇ ᴛᴀᴋᴇ ᴀ ᴀᴄᴛɪᴏɴ ᴀɢᴀɪɴꜱᴛ ᴛʜɪꜱ ʙɪᴛᴄʜ")
        except Unauthorized:
            pass
        
        return await query.answer("𝚃ʜɪꜱ ᴡʜɪꜱᴘᴇʀ ɪꜱ ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙɪᴛᴄʜ🤌🏻", show_alert=True)
    
    search_msg = f"{from_user}_{to_user}"
    
    try:
        msg = whisper_db[search_msg]
    except:
        msg = "🚫 𝙴ʀʀᴏʀ!\n\nᴡʜɪꜱᴘᴇʀ ʜᴀꜱ ʙᴇᴇɴ ᴅᴇʟᴇᴛᴇᴅ ꜰʀᴏᴍ ᴛʜᴇ ᴅᴀᴛᴀʙᴀꜱᴇ!"
    
    SWITCH = InlineKeyboardMarkup([[InlineKeyboardButton("𝙶ᴏ ᴛᴏ ɪɴʟɪɴᴇ", switch_inline_query_current_chat="")]])
    
    await query.answer(msg, show_alert=True)
    
    if len(data) > 3 and data[3] == "one":
        if user_id == to_user:
            await query.edit_message_text("📭 𝚆ʜɪꜱᴘᴇʀ ʜᴀꜱ ʙᴇᴇɴ ʀᴇᴀᴅ!\n\n𝙿ʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ ꜱᴇɴᴅ ᴀ ᴡʜɪꜱᴘᴇʀ!", reply_markup=SWITCH)


async def in_help():
    answers = [
        InlineQueryResultArticle(
            title="🔐 𝚆ʜɪꜱᴘᴇʀ",
            description=f"@Gojo_proxbot [USERNAME | ID] [TEXT]",
            input_message_content=InputTextMessageContent(f"**🧃 𝚄ꜱᴀɢᴇ:**\n\n@Gojo_proxbot (Target Username or ID) (Your Message).\n\n**Example:**\n@Gojo_proxbot @username  Wanna be Your"),
            thumb_url="https://telegra.ph/file/5406ed880a8089c6add3b.jpg",
            reply_markup=switch_btn
        )
    ]
    return answers


@pgram.on_inline_query()
async def bot_inline(_, inline_query):
    string = inline_query.query.lower()
    
    if string.strip() == "":
        answers = await in_help()
        await inline_query.answer(answers)
    else:
        answers = await _whisper(_, inline_query)
        await inline_query.answer(answers[-1], cache_time=0)
                                               
