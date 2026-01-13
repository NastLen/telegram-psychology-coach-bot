"""
Advanced version of main.py with environment variables support
(Optional - use if you want to use .env file)

To use this version:
1. Install python-dotenv: pip install python-dotenv
2. Copy .env.example to .env
3. Fill in your values in .env
4. Run: python main_env.py instead of main.py
"""
import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import router

# Load environment variables
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID", 0)) or None

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables!")

# Enable logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def set_default_commands(bot: Bot):
    """Set default commands for the bot"""
    commands = [
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)

async def main():
    """Main function to run the bot"""
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    dp.include_router(router)
    await set_default_commands(bot)
    
    try:
        logger.info("Bot started polling...")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
