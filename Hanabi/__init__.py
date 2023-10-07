import logging
import time

from pyrogram import Client

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%b/%y %H:%M:%S",
    handlers=[logging.FileHandler("Hanabi.log"), logging.StreamHandler()],
)
logging.getLogger("pyrogram").setLevel(logging.INFO)

START_TIME = time.time()

bot: Client = None