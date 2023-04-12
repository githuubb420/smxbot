from typing import Union
from datetime import datetime
from pyrogram.types import Message
import speedtest
from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)
from ..config import prefixs, sub_chat, sudoers


sudofilter = filters.user(sudoers)

button_a2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="search here", switch_inline_query_current_chat="",
            )
        ],[
            InlineKeyboardButton(
                text="search in chat", switch_inline_query="",
            ),
        ],
    ]
)


@Client.on_message(filters.command(["start", "restart"], prefixs) & filters.private)
async def intro_msg(_, update: Message):
    match = str(update.chat.id)
    with open("users.txt", "a+") as file:
        file.seek(0)
        line = file.read().splitlines()
        if match in line:
            print(f"User {match} is using the bot")
        else:
            file.write(match + "\n")
    
    method = update.reply_text
    text = f"👋🏻 Hi {update.from_user.first_name}!\n\nUse this bot to download videos from the pornhub.com site by providing the name of the video you want to download or you can also search for the video you want to download via inline mode."
    await method(text, reply_markup=button_a2)



@Client.on_message(filters.command("help", prefixs))
async def command_list(_, update: Message):
    text_1 = """
🛠 Command list:

» /start - start this bot
» /help  - showing this message
» /ping  - check bot status
    """
    text_2 = """
🛠 Command list:

» /start - start this bot
» /help  - showing this message
» /ping  - check bot status
» /stats - show bot statistic
» /speed - show speed
» /gcast - broadcast message
    """
    if update.from_user.id in sudoers:
        await update.reply_text(text_2)
    else:
        await update.reply_text(text_1)



@Client.on_message(filters.command("speedtest"))
async def speedtest_command(client, message):
    st = speedtest.Speedtest()
    download_speed = st.download() / 1024 / 1024
    upload_speed = st.upload() / 1024 / 1024
    await message.reply_text(f"My download speed is {download_speed:.2f} Mbps and my upload speed is {upload_speed:.2f} Mbps.")


