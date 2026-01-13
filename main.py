"""
Main bot application
"""
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import router

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
    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Register router
    dp.include_router(router)
    
    # Set default commands
    await set_default_commands(bot)
    
    try:
        logger.info("Bot started polling...")
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
