"""
Main bot application with FastAPI web server
"""
import asyncio
import logging
import os
import threading
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from fastapi import FastAPI
import uvicorn
from config import BOT_TOKEN
from handlers import router

# Enable logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI()

# Global bot and dispatcher
bot = None
dp = None

@app.get("/")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "bot": "running"}

@app.get("/health")
async def health():
    """Health endpoint for Render"""
    return {"status": "healthy"}

async def set_default_commands():
    """Set default commands for the bot"""
    commands = [
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)

async def start_bot():
    """Start bot polling in async context"""
    global bot, dp
    
    # Initialize bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Register router
    dp.include_router(router)
    
    # Set default commands
    await set_default_commands()
    
    try:
        logger.info("🤖 Bot started polling...")
        # Disable signal handling to avoid conflicts in multi-threaded environment (Render + Uvicorn)
        await dp.start_polling(
            bot, 
            allowed_updates=dp.resolve_used_update_types(),
            handle_signals=False  # Отключаем обработку SIGINT/SIGTERM
        )
    except Exception as e:
        logger.error(f"Bot error: {e}")
    finally:
        await bot.session.close()

def run_bot():
    """Run bot in separate event loop"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(start_bot())
    finally:
        loop.close()

def run_web_server():
    """Run FastAPI web server"""
    port = int(os.getenv("PORT", 8000))
    logger.info(f"🌐 Starting web server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

if __name__ == "__main__":
    # Start bot in a separate thread
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Run web server in main thread
    run_web_server()

