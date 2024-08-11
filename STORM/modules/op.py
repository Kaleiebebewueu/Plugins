from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(
    filters.command(["op"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def op(client: Client, message: Message):
    e = await message.edit("4st")
    await e.edit("4sᴛ")
    await e.edit("ᴏᴘ")
    await e.edit("ʙᴀᴋᴋɪ")
    await e.edit("sᴀʙ")
    await e.edit("ʟᴀɴᴅ ᵏⁱ")
    await e.edit("ᴛᴏᴘɪ")
    await e.edit("4‌sᴛ ᴏᴘ ʙᴀᴋᴋɪ sᴀʙ ʟᴀɴᴅ ᴋɪ ᴛᴏᴘɪ....!!")