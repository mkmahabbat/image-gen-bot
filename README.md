# Telegram Gemini Image Bot

A Telegram bot that generates images using Google's Gemini AI based on user text prompts.

## Features

- Generate high-quality images from text descriptions
- Easy-to-use Telegram interface
- Powered by Google Gemini AI
- Deployed on Render.com

## Setup

### Prerequisites

- Python 3.11+
- Telegram Bot Token
- Google Gemini API Key

### Local Development

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables:
   ```bash
   export TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
   export GEMINI_API_KEY="your_gemini_api_key"
   ```
4. Run the bot:
   ```bash
   python bot.py
   ```

### Deployment on Render

1. Fork this repository to your GitHub account
2. Connect your GitHub account to Render
3. Create a new Background Worker service
4. Connect your forked repository
5. Set the following environment variables in Render:
   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
   - `GEMINI_API_KEY`: Your Google Gemini API key
6. Deploy!

## Usage

1. Start a conversation with your bot on Telegram
2. Send `/start` to begin
3. Send any text description of an image you want to generate
4. Wait for the bot to generate and send your image

## Commands

- `/start` - Start the bot and get welcome message
- `/help` - Show help information

## Example Prompts

- "A sunset over mountains"
- "A cute cat wearing a hat"
- "A futuristic city at night"
- "A peaceful lake with reflection"

## API Keys Used

- Telegram Bot Token: `7845413014:AAHO81Yh_uF6ndyTHxlAH5-LnCTb5JOEkE0`
- Gemini API Key: `AIzaSyAdjBQriKrIJZlhgSZD-KcFCKCIh9kIrSY`

## License

MIT License

