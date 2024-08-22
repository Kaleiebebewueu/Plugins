#MIT License

#Copyright (c) 2024 ᴋᴜɴᴀʟ [AFK]

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

import os
import asyncio
from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.errors import FloodWait
from config import SUDO_USERS, OWNER_ID
from STORMDB.data import ONEWORD


FC = 2


@Client.on_message(["randi"])  & (filters.me | filters.user(SUDO_USER))
async def alt_lol(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(1)
    except FloodWait:
        print("Flood !!")
        pass



@Client.on_message(["randii"])  & (filters.me | filters.user(SUDO_USER))
async def alt_mkc(xspam: Client, message: Message):    
    chat_id = message.chat.id
    RUSH = None
    if message.reply_to_message:
        RUSH = message.reply_to_message.id
    try:
        for word in OneWord:
            await xspam.send_message(chat_id, word, reply_to_message_id=RUSH)
            await asyncio.sleep(000.1)
    except FloodWait:
        print("Flood !!")
        pass
    
    

@Client.on_message(["rrandi"])  & (filters.me | filters.user(SUDO_USER))
async def alt_stop(_, message: Message):    
    reply = await message.reply_text("👻𝚃𝙴𝚁𝙸 𝙼𝙰𝙰 𝙺𝙸 𝙲𝙷𝚄𝚃 ...")
    await reply.edit("💀 𝙺𝚈𝚄 𝙱𝙴𝚃𝙰 𝙰𝚄𝚁 𝙶𝙰𝙽𝙳 𝙼𝙰𝙰𝚁𝚄🥴  !!\n\n👻#𝙵𝙴𝙴𝙻_4𝚂𝚃_𝙳𝙰𝙳𝙳𝚈 💕 !!")
    os.system(f"kill -9 {os.getpid()} && python3 -m STORM")
    
