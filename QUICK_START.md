# 🚀 QUICK START GUIDE

## За 5 минут до запуска

### Шаг 1: Установка (2 минуты)

```bash
# Перейти в папку проекта
cd telegram-service-bot

# Установить зависимости
pip install -r requirements.txt
```

### Шаг 2: Конфигурация (2 минуты)

1. **Открыть `config.py`** в текстовом редакторе
2. **Найти ваш Admin ID:**

   - Написать боту @userinfobot
   - Скопировать User ID
   - Вставить в `config.py` вместо `None`:

   ```python
   ADMIN_CHAT_ID = 123456789  # Ваш ID
   ```

3. **Обновить ссылки:**

   ```python
   BOOKING_URL = "https://calendly.com/your-profile"
   WEBSITE_URL = "https://your-website.com"
   WHATSAPP_URL = "https://wa.me/+49123456789"
   EMAIL = "your@email.com"
   ```

4. **Отредактировать текст:**
   - ABOUT_TEXT - о вас
   - SERVICES_TEXT - услуги и цены
   - FAQ_TEXT - ответы на вопросы
   - CONTACT_TEXT - контакты

### Шаг 3: Запуск (1 минута)

```bash
python main.py
```

Бот начнёт слушать сообщения. Готово! 🎉

---

## 📱 Как тестировать

1. Найти своего бота в Telegram (по имени)
2. Написать `/start`
3. Кликнуть на кнопки
4. Заполнить форму
5. Проверить, что уведомления приходят в admin chat

---

## 🎨 Кастомизация (опционально)

### Изменить текст кнопок

В `config.py`:

```python
BTN_ABOUT = "ℹ️ About"  # Изменить здесь
```

### Добавить новую кнопку в главное меню

1. Добавить переменную в `config.py`:

   ```python
   BTN_PORTFOLIO = "🎨 Portfolio"
   ```

2. Добавить кнопку в клавиатуру в `keyboards.py`:

   ```python
   [KeyboardButton(text=BTN_PORTFOLIO)]
   ```

3. Добавить обработчик в `handlers.py`:
   ```python
   @router.message(F.text == "🎨 Portfolio")
   async def portfolio_handler(message: Message):
       await message.answer("Ссылка на портфель...", reply_markup=...)
   ```

---

## 💾 Развертывание на сервер

Когда будет готово к production:

### Вариант 1: VPS (DigitalOcean, Linode, AWS)

```bash
# На сервере:
sudo apt-get install python3 python3-pip
git clone <your-repo>
cd telegram-service-bot
pip install -r requirements.txt

# Запустить в фоне (например, через screen):
screen -S bot
python main.py
# Ctrl+A+D для выхода

# Или через systemd (для автозапуска):
# Создать /etc/systemd/system/tgbot.service
```

### Вариант 2: Docker

```bash
docker build -t coach-bot .
docker run -d --name coach-bot coach-bot
```

### Вариант 3: Heroku/PythonAnywhere

Загрузить файлы, установить зависимости, запустить `main.py`

---

## 📊 Структура данных

Когда пользователь отправляет форму/вопрос, админу приходит сообщение:

```
❓ Новый вопрос от пользователя

👤 User ID: 123456789
📛 Имя: John
📝 Вопрос: How does it work?
```

Можно ответить напрямую пользователю в Telegram.

---

## 🐛 Если что-то не работает

1. **Проверить ошибки в терминале** - обычно там подсказка
2. **Bot token** - верно ли скопирован?
3. **ADMIN_CHAT_ID** - правильный ли ID?
4. **Python версия** - минимум 3.9

---

## 📚 Дальнейшие улучшения

- [ ] Добавить расписание работы
- [ ] Интеграция с реальной БД (вместо in-memory)
- [ ] История переписки
- [ ] Автоответчик за пределами рабочих часов
- [ ] Интеграция с Calendly API (проверка доступности)
- [ ] Платежи напрямую в боте (через Stripe/Paypal)
- [ ] Многоязычность (переключение EN/RU/DE)
- [ ] Аналитика (кол-во посещений, конверсия)

---

## 📞 Технподдержка

- **Документация aiogram:** https://docs.aiogram.dev/
- **Telegram Bot API:** https://core.telegram.org/bots/api
- **Python документация:** https://docs.python.org/

---

**Вопросы? Нужна помощь? Проверьте README.md для подробной документации.**
