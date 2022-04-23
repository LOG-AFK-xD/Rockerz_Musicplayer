import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from modules.config import BOT_USERNAME
START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a9c008bacbb44f547639e.jpg",
        caption=f"""<b>Hello Friends {message.from_user.mention} 😉️!</b>
I'm The Ankit & Khushi Music Bot! A Powerful Bot to Play Music in Your Group Voice Chat 😇!

POWERED BY- [ANKIT & KHUSHI](T.ME/ANKIT_KHUSHI) .""",
   reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "🔰️ Support 🔰️", url=f"https://t.me/UNIQUE_SOCIETY"
                    ),
                    InlineKeyboardButton(
                        "⚜️ Channel ⚜️", url="https://t.me/ITZZ_OFFICIAL"
                    )
                ]
            ]
        )
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "sᴀʟɪᴍ"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/a9c008bacbb44f547639e.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✦ Join Here And Support ✦", url=f"https://t.me/UNIQUE_SOCIETY")
                ]
            ]
        ),
    )
