from config import SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["like"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def like(_, e: Message):       
      Fuk = await e.reply("⚡")
      await Fuk.edit_text(f"‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n██████▄▄█‡‡‡‡‡‡████████▄\n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n█████‡‡‡‡‡‡‡██████████")