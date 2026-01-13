# Configuration for Psychology Coach Telegram Bot

# Bot Token (from BotFather)
BOT_TOKEN = "8538542036:AAEOnFstif9BBcfoSYV4DK0i_icM4Sw6Tqs"

# Admin chat ID (where form submissions and questions go)
# Set this to your Telegram user ID or group ID
ADMIN_CHAT_ID = None  # Replace with actual chat ID (e.g., 123456789)

# External links
BOOKING_URL = "https://calendly.com/mindcare-berlin/consultation"  # Calendly ссылка
WEBSITE_URL = "https://mindcare-berlin.example.com"  # Вебсайт
PAYMENT_URL = "https://mindcare-berlin.example.com/pricing"  # Страница оплаты
WHATSAPP_URL = "https://wa.me/493012345678"  # WhatsApp: +49 30 12345678
EMAIL = "elena.kravtsova@example.com"  # Психолог Елена Кравцова

# Content (easily editable)
ABOUT_TEXT = """
� Психолог и коуч

🎯 Мой подход
Интегративная психология + практический коучинг для взрослых, работающих в креативных и IT-профессиях.

📈 Опыт
7+ лет индивидуальной работы, сертифицирован в нескольких направлениях.

💡 Основные темы
✓ Тревога, стресс, выгорание
✓ Уверенность в себе и самооценка
✓ Карьерные решения
✓ Личные отношения
✓ Жизненный баланс

🇷🇺 🇬🇧 Работаю на русском и английском языках
"""

SERVICES_TEXT = """
📋 Форматы работы

1️⃣ Разовая консультация
⏱ 60 минут
💻 Онлайн или оффлайн (Берлин)
💶 €80

2️⃣ Пакет из 4 сессий
⏱ 4 × 60 минут
💶 €300 (экономия €20)
📍 Углублённая работа

📌 Варианты проведения
🌍 Online — Zoom/Skype (из любой точки мира)
📍 Offline — кабинет в центре Берлина

💳 Полная информация о ценах на сайте
"""

FAQ_TEXT = """
❓ Часто задаваемые вопросы

❓ Как это работает?
1. Вы забронируете время через календарь
2. За день до сессии вы получите ссылку для встречи
3. Мы встретимся и поговорим о ваших вопросах
4. После сессии я пришлю вам заметки и рекомендации

❓ Как подготовиться?
• Если это первая встреча — просто приходите спокойно
• Минимум отвлекающих факторов (для онлайн)
• Список вопросов пойдёт на пользу

❓ Политика отмены
• Отмену/перенос за 48 часов — бесплатно
• Отмена менее чем за 48 часов — сессия оплачивается
• Форс-мажор обсуждается индивидуально

❓ На каких языках?
🇷🇺 Русский
🇬🇧 English
(можно переходить между языками на одной сессии)
"""

CONTACT_TEXT = """
📞 Контакты

Есть вопросы перед бронированием? Напишите мне:

📧 Email: {email}
💬 WhatsApp: нажмите кнопку ниже

Или задайте вопрос прямо боту — я передам его менеджеру.
""".format(email=EMAIL)

# Keyboard buttons text (все на русском)
BTN_ABOUT = "ℹ️ О психологе"
BTN_SERVICES = "💼 Услуги"
BTN_FAQ = "❓ Вопросы & ответы"
BTN_CONTACT = "📞 Контакты"
BTN_BOOK = "📅 Забронировать"
BTN_LEAD_FORM = "📝 Оставить запрос"

# Button texts
BTN_BOOK_LINK = "📅 Открыть календарь"
BTN_WEBSITE = "🌐 Веб-сайт"
BTN_WHATSAPP = "💬 WhatsApp"
BTN_EMAIL = "📧 Email"
BTN_ASK_QUESTION = "❓ Задать вопрос"
BTN_BACK = "⬅️ Назад"
BTN_SUBMIT_FORM = "✅ Отправить"
BTN_CANCEL = "❌ Отмена"
