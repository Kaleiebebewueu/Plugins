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

from pyrogram import Client, filters
from config import SUDO_USERS

@Client.on_message(
    filters.command(["bstats"], ".") & (filters.me | filters.user(SUDO_USERS))
)
async def bstats(client, message):
    msg = f"""
        ➖➖➖➖➖➖➖➖➖➖➖➖➖
        **         ❄️ sᴀɴᴀᴛᴀɴɪ ᴜꜱᴇʀʙᴏᴛ ‌❄️ **
        ➖➖➖➖➖➖➖➖➖➖➖➖➖
        **• ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `3.11.3`
        **• ᴜꜱᴇʀʙᴏᴛ ᴠᴇʀꜱɪᴏɴ :** `M.2.1.1`
        **• ɢʀᴏᴜᴘ : [sᴀɴᴀᴛᴀɴɪ ᴄʜᴀᴛᴢ](https://t.me/+Ckzm2ypQyIIzZTll) **
        **• ᴄʜᴀɴɴᴇʟ : [sᴀɴᴀᴛᴀɴɪ ᴛᴇᴄʜ](https://t.me/ALL_SANATANI_BOT) **
        **• ᴏᴡɴᴇʀ : [sᴀᴄʜɪɴ sᴀɴᴀᴛᴀɴɪ](https://t.me/V_VIP_OWNER) **
        ➖➖➖➖➖➖➖➖➖➖➖➖➖
            """
    await message.reply(msg)
