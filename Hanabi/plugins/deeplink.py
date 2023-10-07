from pyrogram import Client, filters, types, enums, errors


@Client.on_message(filters.command("start") & filters.private)
async def start_command(_, message: types.Message):
    await message.reply_text("Hello!")