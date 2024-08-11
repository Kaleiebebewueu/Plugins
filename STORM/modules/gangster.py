from pyrogram import Client, filters
from pyrogram.types import Message
from config import SUDO_USERS

@Client.on_message(
    filters.command(["geng"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def geng(client: Client, message: Message):
    e = await message.edit("ᴇᴠᴇʀʏ-ʙᴏᴅʏ")
    await e.edit("ɪs")
    await e.edit("ɢᴀɴɢsᴛᴜʀ")
    await e.edit("ᴜɴᴛɪʟ")
    await e.edit("4sᴛ")
    await e.edit("ғɪɢʜᴛᴇʀ")
    await e.edit("🔥🔥🔥")
    await e.edit("ᴇᴠᴇʀʏ-ʙᴏᴅʏ ɪs ɢᴀɴɢsᴛᴜʀ ᴜɴᴛɪʟ 4sᴛ ғɪɢʜᴛᴇʀ 🔥🔥🔥")
    