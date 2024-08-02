import logging
import os
from flask import Flask
from pymongo import MongoClient
from telegram.ext import Application, CommandHandler
import stripe
import threading
import asyncio
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGODB_URI"))
db = client.get_database('ecommerce_db')

# Configure Stripe
stripe.api_key = os.getenv("STRIPE_API_KEY")

# Command handler for /start
async def start(update, context):
    logger.info("Received /start command")
    await update.message.reply_text('Hello! Welcome to the E-commerce Bot.')

# Command handler for /help
async def help_command(update, context):
    logger.info("Received /help command")
    await update.message.reply_text('This is a help message.')

async def main():
    application = Application.builder().token(os.getenv("TELEGRAM_BOT_TOKEN")).build()

    # Register commands
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    logger.info("Bot is starting...")

    # Run the bot
    await application.run_polling()

from routes.product_routes import product_bp
from routes.order_routes import order_bp

app.register_blueprint(product_bp)
app.register_blueprint(order_bp)

def run_flask():
    """Run Flask app in a separate thread."""
    logger.info("Starting Flask server...")
    app.run(port=5000, debug=False)  # Disable debug mode to avoid threading issues

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()  # Start Flask in a separate thread

    # Using asyncio.run() to handle the event loop correctly
    try:
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
