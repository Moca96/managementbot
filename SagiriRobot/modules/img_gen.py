from pyrogram import Client, filters

from SagiriRobot import pbot

import httpx





@pbot.on_message(filters.command("gen"))

async def gen_img(client, message):

    temp = await message.reply_text("**Creating, please waitoo...**")

    prompt = message.text.split(maxsplit=1)[1]

    data = {"prompt": prompt}

    async with httpx.AsyncClient(timeout=30) as cli:

        try:

            response = await cli.post("https://alphacoder-api-93747976af25.herokuapp.com/text2img", json=data)

            result = response.json()

            pic = result.get("output_url")[0]

            await client.send_photo(message.chat.id, photo=pic, caption=f"**Image created by @Gojo_proxbot**")

            await temp.delete()

        except Exception as e:

            await temp.edit_text(f"**An error occurred:\n**`{str(e)}`")
