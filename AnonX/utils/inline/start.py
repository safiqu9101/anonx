from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="нοᴡ το υѕє мє? ϲοммαиᴅ мєиυ.", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="🥀 ɢяουᴘ 💥", url=f"http://t.me/DOSTO_KI_PIYAR",
            ),
            InlineKeyboardButton(
                text="🥀 ᴄнαииєʟ 💥", url=f"https://t.me/TaitanXbot",
            )
        ],
        [
            InlineKeyboardButton(
                text="✚ ᴀᴅᴅ мє το ʏουя gяουρ ✚",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ οωиєя ✨",
                url=f"https://t.me/taitangamer",
            ),
            InlineKeyboardButton(
                text="💮 ѕουяϲє 💮",
                url=f"https://t.me/taitangamer",
            )
        ],
     ]
    return buttons
