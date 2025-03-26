from telethon import events, Button, custom
from SagiriRobot.events import register

@register(pattern=("^/(game|games)"))
async def games(event):

    await event.reply(
                    "ʜᴇʏ, ᴡᴇ ᴀᴛᴛᴀᴄʜᴇᴅ ꜱᴏᴍᴇ ɢᴀᴍᴇꜱ ɪɴ ɢᴏᴊᴏ, ᴘʀᴇꜱꜱ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴘʟᴀʏɪɴɢ ɢᴀᴍᴇꜱ.",
                    buttons=[
                        [
                            Button.url(
                                "˹ʙᴜʙʙʟᴇ ᴛᴏᴡᴇʀ 3ᴅ˼",
                                "https://play.famobi.com/bubble-tower-3d",
                            ),
                            Button.url(
                                "˹ʀᴏᴍ ɴᴏᴍ ʀᴜɴ˼",
                                "https://play.famobi.com/om-nom-run",
                            ),
                        ],

                        [
                            Button.url(
                                "˹ᴄᴀɴɴᴏɴ ʙᴀʟʟꜱ 3ᴅ˼",
                                "https://play.famobi.com/cannon-balls-3d",
                            ),
                            Button.url(
                                "˹ᴀʀᴄʜᴇʀʏ ᴡᴏʀʟꜱ ᴛᴏᴜʀ˼",
                                "https://play.famobi.com/archery-world-tour",
                            ),
                        ]
                    ],
                    parse_mode="html",
                )
