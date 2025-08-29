import os
import logging
import asyncio
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TELEGRAM_BOT_TOKEN = "7845413014:AAHO81Yh_uF6ndyTHxlAH5-LnCTb5JOEkE0"
GEMINI_API_KEY = "AIzaSyAdjBQriKrIJZlhgSZD-KcFCKCIh9kIrSY"

# Configure Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    await update.message.reply_text(
        'Hi! I can generate images for you using Google Gemini AI. '
        'Just send me a text description of what you want to see!'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = """
🤖 *Gemini Image Bot*

I can generate images based on your text descriptions using Google's Gemini AI.

*How to use:*
• Send me any text description
• I'll generate an image based on your prompt
• Wait a moment for the magic to happen!

*Examples:*
• "A sunset over mountains"
• "A cute cat wearing a hat"
• "A futuristic city at night"

*Commands:*
/start - Start the bot
/help - Show this help message
    """
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Generate an image based on user's text prompt."""
    user_prompt = update.message.text
    user_name = update.effective_user.first_name
    
    # Send "typing" action to show bot is working
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="upload_photo")
    
    try:
        # Send initial message
        status_message = await update.message.reply_text(
            f"🎨 Generating image for: '{user_prompt}'\nPlease wait..."
        )
        
        # Generate image using Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash-image-preview",
            contents=[user_prompt],
        )
        
        # Check if image was generated
        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                # Get the image data
                image_data = part.inline_data.data
                
                # Send the image to user
                await context.bot.send_photo(
                    chat_id=update.effective_chat.id,
                    photo=BytesIO(image_data),
                    caption=f"🎨 Generated image for: '{user_prompt}'"
                )
                
                # Delete status message
                await status_message.delete()
                return
        
        # If no image was found in response
        await status_message.edit_text(
            "❌ Sorry, I couldn't generate an image for that prompt. "
            "Please try a different description."
        )
        
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        await update.message.reply_text(
            "❌ Sorry, there was an error generating your image. "
            "Please try again later or with a different prompt."
        )

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, generate_image))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()

