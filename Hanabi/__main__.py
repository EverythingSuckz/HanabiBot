import asyncio
from pyrogram import Client, idle

from config import Config
import logging

logger = logging.getLogger(__name__)

async def main():
    import Hanabi
    Hanabi.bot = Client(
        "hanabi",
        api_id=Config.API_ID,
        api_hash=Config.API_HASH,
        bot_token=Config.BOT_TOKEN,
        plugins=dict(root="Hanabi/plugins")
    )
    await Hanabi.bot.start()
    logger.info("Bot Started")
    info = await Hanabi.bot.get_me()
    logger.info("Username: @{} \nID: {}".format(info.username, info.id))
    await idle()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning("Bot stopped.")