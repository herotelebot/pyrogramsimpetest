import os
from pyrogram import Client, filters
#from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from telegraph import upload_file
from pyrogram import Client
from env import EnvData
from AlterMessage import Msg
#from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
#                            InlineKeyboardMarkup, InlineKeyboardButton)

akhilapp1 = Client(
        "FirstBotusingPyrogram",
        bot_token=EnvData.BOT_TOKEN, #"1682813101:AAH0xqB2jhMfJT7XSBCY6-MucQzNHWWnYq0",
        api_id=int(EnvData.API_ID), #"1687826",
        api_hash=EnvData.API_HASH #"1af0252a7f97e288e2fff6b0adad5b2f"
        
)

@akhilapp1.on_message(filters.command(["start"]))
async def start(bot, update):
    text = Msg.START_TEXT.format(update.from_user.mention)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        #reply_markup=reply_markup,
        parse_mode="HTML"
    )


akhilapp1.run()
 
