from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """
✦ ʜᴇʏ ᴛʜᴇʀᴇ, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ᴜʜʜ !

❅ ɪ ᴀᴍ ๛ʙʟᴀᴄᴋʟᴏᴠᴇʀ ᴍᴜsɪᴄ ༗ ᴍ ᴜ s ɪ ᴄ

❅ ɪғ ʏᴏᴜ ᴡᴀɴᴛ ๛ʙʟᴀᴄᴋʟᴏᴠᴇʀ ᴍᴜsɪᴄ ༗ ʙᴏᴛ ʀᴇᴘᴏ, ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴍʏ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.
"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [
          InlineKeyboardButton("🏝sᴜᴘᴘᴏʀᴛ🏝", url="https://t.me/SSC_MAKER_QUIZ"),
          InlineKeyboardButton("🏡ʀᴇᴘᴏ🏡", url="https://t.me/BlackMusicSupport"),
          ],
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/c752663369c7161426044.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
