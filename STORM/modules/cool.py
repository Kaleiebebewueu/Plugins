from config import SUDO_USERS
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.command(["cool"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def cool(_, e: Message):       
      Fuk = await e.reply("⚡")
      await Fuk.edit_text(f"ʙᴏʟᴀ ᴛʜᴀ...!!\nᴊᴄʙ ᴋᴏ ᴋʜᴏᴅɴᴀ 𝐀ᴜʀ 4sᴛ \nᴋᴏ ᴄʜʜᴏᴅɴᴀ ᴀᴀᴄʜᴇ sᴇ ᴀᴀᴛᴀ ʜᴀɪ...!!")
      
      
      
      
