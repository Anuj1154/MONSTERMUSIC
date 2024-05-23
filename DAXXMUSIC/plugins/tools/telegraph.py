from telegraph import upload_file
from pyrogram import filters
from DAXXMUSIC import app
from pyrogram.types import InputMediaPhoto


@app.on_message(filters.command(["tgm" , "link"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("๏ ʟɪɴᴋ ᴏɴ ᴛʜᴇ ᴡᴀʏ ʙʏ ʙʟᴀᴄᴋʟᴏᴠᴇʀ🎌...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'๏ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➠ {url}\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ๛ʙʟᴀᴄᴋʟᴏᴠᴇʀ ᴍᴜsɪᴄ࿐')

########____________________________________________________________######

@app.on_message(filters.command(["graph" , "grf"]))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("๏ ʟɪɴᴋ ᴏɴ ᴛʜᴇ ᴡᴀʏ ʙʏ ʙʟᴀᴄᴋʟᴏᴠᴇʀ🎌...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://graph.org" + x

        i.edit(f'๏ ʏᴏᴜʀ ɢʀᴀᴘʜ ᴜʀʟ ɪs ʀᴇᴀᴅʏ ʙᴀʙʏ ➠ {url}\n\n๏ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➠ ๛ʙʟᴀᴄᴋʟᴏᴠᴇʀ ᴍᴜsɪᴄ࿐')

