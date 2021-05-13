from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAEJk31giDbxyx3MGVI7Ws77DcYAAVpTVo8AAlkAA8VDGj2DjvM8O4zu9x8E")
    await message.reply_sticker("CAACAgQAAxkBAAEJ3C9gnTkTPoOciaMVQwa6_k6F56vb6wAChxcAAtqjlSz9pNTIjJLj")
    await message.reply_sticker("CAACAgUAAxkBAAEJ3DNgnTl8ZD4mV95BGFr4UIbW2nGPXgACwgEAAhsSOVWQaeEVO8RSkR8E")
    await message.reply_sticker("CAACAgIAAxkBAAEJ3DlgnTop9s8G5FQOpNqp5JaeXM1LdAACIgMAAm2wQgO8x8PfoXC1eB8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chat
Maintained by @hayper007 ❤
\nTo add in your group contact us at @hayper007.
\nHit /help list of available commands.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Music World", url="https://t.me/Zxmodeapk",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Films_requested"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Zxmodeapk"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/kingboyss/VCTGBOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/TheMp3Playebot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Zxmodeapk"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Zxmodeapk"
                    )
                ]
            ]
        )
    )    
