# Telegram Service Bot Configuration

## Quick Start

### 1. Prerequisites

- Python 3.9+
- pip or poetry

### 2. Installation

```bash
# Clone the repository or navigate to project directory
cd telegram-service-bot

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Edit `config.py` and fill in your details:

```python
# Required settings:
ADMIN_CHAT_ID = 123456789  # Get your Telegram ID from @userinfobot

# External links (customize as needed):
BOOKING_URL = "https://calendly.com/your-coach"
WEBSITE_URL = "https://your-website.com"
PAYMENT_URL = "https://your-website.com/pricing"
WHATSAPP_URL = "https://wa.me/+49XXXXXXXXXX"
EMAIL = "your.email@example.com"

# Content (edit the text strings):
ABOUT_TEXT = "..."  # Your bio and approach
SERVICES_TEXT = "..."  # Services and pricing
FAQ_TEXT = "..."  # FAQ content
CONTACT_TEXT = "..."  # Contact info
```

### 4. Run the Bot

```bash
python main.py
```

The bot will start polling and wait for messages.

---

## File Structure

```
telegram-service-bot/
├── main.py              # Entry point - starts the bot
├── config.py            # Configuration, links, and content
├── handlers.py          # All command and message handlers
├── keyboards.py         # Button layouts for messages
├── database.py          # User state management
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

---

## Features

### 🎯 Main Menu

- **About** - Information about you and your approach
- **Services** - Service formats and pricing
- **FAQ** - Common questions
- **Contact** - Direct messaging options
- **Book Now** - Link to booking page
- **Leave a Request** - Form to submit inquiry

### 📋 About Section

Shows your profile, experience, main topics, and languages.

### 💼 Services

Lists:

- Single session details
- Package options
- Online/Offline options
- Pricing

### ❓ FAQ

Includes answers to:

- How it works
- How to prepare
- Cancellation policy
- Languages

### 📞 Contact Options

- WhatsApp link
- Email
- Ask a question (goes to admin)

### 📅 Book Now

Directs to Calendly or your booking page.

### 📝 Lead Form

Collects:

- Name
- Contact info
- Brief request
- Sends to admin

---

## Customization

### Adding/Editing Content

Edit in `config.py`:

```python
ABOUT_TEXT = """Your text here"""
SERVICES_TEXT = """Your text here"""
FAQ_TEXT = """Your text here"""
```

Use HTML tags for formatting:

- `<b>bold</b>`
- `<i>italic</i>`
- `<u>underline</u>`
- `<code>code</code>`

### Changing Button Text

Edit in `config.py` (lines starting with `BTN_`):

```python
BTN_ABOUT = "ℹ️ About"
BTN_SERVICES = "💼 Services"
# etc.
```

### Adding External Links

Update in `config.py`:

```python
BOOKING_URL = "https://your-calendly.com"
WHATSAPP_URL = "https://wa.me/+49123456789"
EMAIL = "your@email.com"
```

### Setting Admin Notifications

Find your Telegram user ID:

1. Send a message to @userinfobot
2. It will show your ID
3. Put it in `config.py`:

```python
ADMIN_CHAT_ID = 123456789
```

Now, when users submit forms or ask questions, you'll receive notifications.

---

## How the Flow Works

### Booking Flow

```
User taps "Book Now"
    ↓
Sees inline button "📅 Open Calendar"
    ↓
Redirected to Calendly/booking page
    ↓
Selects time slot and pays on your website
```

### Question/Form Flow

```
User sends question or form
    ↓
Data goes to your admin chat
    ↓
You can respond directly to the user's Telegram ID
```

---

## Deployment

### Option 1: Local Server (Testing)

Just run `python main.py` on your computer. Bot works while script is running.

### Option 2: Cloud Deployment (Production)

**Heroku** (free tier ended, use alternative)
**PythonAnywhere** (free tier available)

```bash
# Upload files, set environment variables, run main.py
```

**Docker** (any VPS):

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

**DigitalOcean, AWS, Linode** etc:

- Rent a server ($3-5/month)
- SSH in, install Python
- Clone project, install deps, run main.py in screen/tmux

---

## Troubleshooting

### Bot doesn't respond

1. Check `BOT_TOKEN` is correct in `config.py`
2. Run `python main.py` and look for errors
3. Check bot is still running (it should print "Bot started polling...")

### Admin notifications not working

1. Make sure `ADMIN_CHAT_ID` is set correctly
2. Test by sending a message to the bot yourself
3. Check you have the correct Telegram user ID (use @userinfobot)

### Keyboard buttons don't show

1. Check button text matches exactly in both `config.py` and `keyboards.py`
2. Make sure `reply_markup` is being passed to `message.answer()`

### Links not clickable

- Use inline buttons for links (they'll appear as blue clickable buttons)
- Regular buttons are for commands only

---

## Tech Stack

- **Framework:** aiogram v3
- **Language:** Python 3.9+
- **Async:** asyncio
- **Logging:** Python logging module

---

## Support

For aiogram documentation: https://docs.aiogram.dev/

---

## License

Use this bot for your coaching/psychology practice freely.

Last Updated: January 2026
