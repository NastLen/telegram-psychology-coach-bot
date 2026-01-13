"""
Main bot handlers
"""
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from config import (
    ABOUT_TEXT, SERVICES_TEXT, FAQ_TEXT, CONTACT_TEXT,
    BOOKING_URL, WEBSITE_URL, PAYMENT_URL, WHATSAPP_URL, EMAIL,
    BTN_BACK, ADMIN_CHAT_ID
)
from keyboards import (
    get_main_menu_keyboard, get_booking_inline_keyboard,
    get_contact_inline_keyboard, get_services_inline_keyboard,
    get_question_cancel_keyboard
)
from database import get_user_state, reset_user_state

router = Router()

# Define FSM states for forms
class QuestionForm(StatesGroup):
    asking_question = State()

class LeadForm(StatesGroup):
    asking_name = State()
    asking_contact = State()
    asking_request = State()
    confirming = State()

# ===== START & HELP =====
@router.message(Command("start"))
async def cmd_start(message: Message):
    """Start command - show main menu"""
    welcome_text = """
👋 MindCare Assistant

Демонстрационный проект разработан Анастасией Булаткиной.

На примере психолога Елены Кравцовой этот бот помогает клиентам узнать об услугах психологического консультирования и быстро забронировать консультацию.

Выберите, что вас интересует:
"""
    await message.answer(welcome_text, reply_markup=get_main_menu_keyboard())

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Help command"""
    help_text = """
<b>📚 Что я умею:</b>

<b>ℹ️ О психологе</b> — узнать о специалисте и подходе
<b>💼 Услуги</b> — форматы работы и цены
<b>❓ Вопросы & ответы</b> — ответы на частые вопросы
<b>📞 Контакты</b> — способы связи со мной
<b>📅 Забронировать</b> — перейти к бронированию консультации
<b>📝 Оставить запрос</b> — заполнить форму запроса

Введите /start для главного меню.
"""
    await message.answer(help_text, reply_markup=get_main_menu_keyboard())

# ===== MAIN MENU BUTTONS =====
@router.message(F.text == "ℹ️ О психологе")
async def about_handler(message: Message):
    """About me"""
    await message.answer(ABOUT_TEXT, reply_markup=get_main_menu_keyboard(), parse_mode="HTML")

@router.message(F.text == "💼 Услуги")
async def services_handler(message: Message):
    """Services and pricing"""
    await message.answer(
        SERVICES_TEXT,
        reply_markup=get_services_inline_keyboard(BOOKING_URL, PAYMENT_URL),
        parse_mode="HTML"
    )

@router.message(F.text == "❓ Вопросы & ответы")
async def faq_handler(message: Message):
    """FAQ"""
    await message.answer(FAQ_TEXT, reply_markup=get_main_menu_keyboard(), parse_mode="HTML")

@router.message(F.text == "📞 Контакты")
async def contact_handler(message: Message):
    """Contact information"""
    contact_message = f"""
📞 Контакты

Быстрые способы связи:

💬 WhatsApp: нажмите кнопку ниже
📧 Email: elena.kravtsova@example.com
💭 Или задайте вопрос прямо боту — я передам его менеджеру
"""
    
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    
    buttons = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💬 Написать WhatsApp", url=WHATSAPP_URL)],
            [InlineKeyboardButton(text="❓ Задать вопрос боту", callback_data="ask_question")],
        ]
    )
    
    await message.answer(contact_message, reply_markup=buttons)

@router.message(F.text == "📅 Забронировать")
async def book_handler(message: Message):
    """Booking"""
    booking_text = """
📅 <b>Забронировать консультацию</b>

Нажмите кнопку ниже, чтобы выбрать удобное время в календаре:
"""
    await message.answer(
        booking_text,
        reply_markup=get_booking_inline_keyboard(BOOKING_URL, WEBSITE_URL, BOOKING_URL),
        parse_mode="HTML"
    )

# ===== ASK QUESTION =====
@router.callback_query(F.data == "ask_question")
async def ask_question_callback(callback: CallbackQuery, state: FSMContext):
    """Start asking a question"""
    await state.set_state(QuestionForm.asking_question)
    await callback.message.answer(
        "📝 Напишите ваш вопрос. Я передам его менеджеру, и вас свяжутся в ближайшее время.",
        reply_markup=get_question_cancel_keyboard()
    )
    await callback.answer()

@router.message(QuestionForm.asking_question, F.text != "❌ Отмена")
async def question_received(message: Message, state: FSMContext, bot):
    """Receive question and send to admin"""
    question_text = f"""
❓ <b>Новый вопрос от пользователя</b>

👤 <b>User ID:</b> {message.from_user.id}
📛 <b>Имя:</b> {message.from_user.first_name}
📝 <b>Вопрос:</b>

{message.text}
"""
    
    if ADMIN_CHAT_ID:
        try:
            await bot.send_message(ADMIN_CHAT_ID, question_text, parse_mode="HTML")
        except Exception as e:
            print(f"Error sending to admin: {e}")
    
    await message.answer(
        "✅ Спасибо! Ваш вопрос отправлен менеджеру. Мы ответим вам в ближайшее время.",
        reply_markup=get_main_menu_keyboard()
    )
    await state.clear()

@router.message(QuestionForm.asking_question, F.text == "❌ Отмена")
async def cancel_question(message: Message, state: FSMContext):
    """Cancel question"""
    await message.answer("Отменено.", reply_markup=get_main_menu_keyboard())
    await state.clear()

# ===== LEAD FORM =====
@router.message(F.text == "📝 Оставить запрос")
async def lead_form_start(message: Message, state: FSMContext):
    """Start lead form"""
    await state.set_state(LeadForm.asking_name)
    await message.answer(
        "📝 <b>Оставить заявку</b>\n\nПожалуйста, введите ваше имя:",
        reply_markup=get_question_cancel_keyboard(),
        parse_mode="HTML"
    )

@router.message(LeadForm.asking_name, F.text != "❌ Отмена")
async def lead_form_name(message: Message, state: FSMContext):
    """Receive name"""
    user_state = get_user_state(message.from_user.id)
    user_state.name = message.text
    
    await state.set_state(LeadForm.asking_contact)
    await message.answer(
        "Как с вами связаться? (Email, телефон, Telegram или WhatsApp):",
        reply_markup=get_question_cancel_keyboard()
    )

@router.message(LeadForm.asking_contact, F.text != "❌ Отмена")
async def lead_form_contact(message: Message, state: FSMContext):
    """Receive contact"""
    user_state = get_user_state(message.from_user.id)
    user_state.contact = message.text
    
    await state.set_state(LeadForm.asking_request)
    await message.answer(
        "Кратко опишите, что вас интересует или какую проблему вы хотели бы решить:",
        reply_markup=get_question_cancel_keyboard()
    )

@router.message(LeadForm.asking_request, F.text != "❌ Отмена")
async def lead_form_request(message: Message, state: FSMContext):
    """Receive request"""
    user_state = get_user_state(message.from_user.id)
    user_state.request = message.text
    
    # Show confirmation
    confirmation = f"""
<b>Проверьте ваши данные:</b>

📛 <b>Имя:</b> {user_state.name}
📞 <b>Контакт:</b> {user_state.contact}
📝 <b>Запрос:</b> {user_state.request}

Отправить?
"""
    
    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Да"), KeyboardButton(text="❌ Отмена")]
        ],
        resize_keyboard=True
    )
    
    await state.set_state(LeadForm.confirming)
    await message.answer(confirmation, reply_markup=keyboard, parse_mode="HTML")

@router.message(LeadForm.confirming, F.text == "✅ Да")
async def lead_form_confirm(message: Message, state: FSMContext, bot):
    """Confirm and send to admin"""
    user_state = get_user_state(message.from_user.id)
    
    admin_text = f"""
📋 <b>Новая заявка</b>

👤 <b>Telegram ID:</b> {message.from_user.id}
📛 <b>Имя:</b> {user_state.name}
📞 <b>Контакт:</b> {user_state.contact}
📝 <b>Запрос:</b>
{user_state.request}
"""
    
    if ADMIN_CHAT_ID:
        try:
            await bot.send_message(ADMIN_CHAT_ID, admin_text, parse_mode="HTML")
        except Exception as e:
            print(f"Error sending form to admin: {e}")
    
    await message.answer(
        "✅ Спасибо! Ваша заявка отправлена. Мы свяжемся с вами в ближайшее время.",
        reply_markup=get_main_menu_keyboard()
    )
    
    reset_user_state(message.from_user.id)
    await state.clear()

@router.message(LeadForm.confirming, F.text == "❌ Отмена")
async def lead_form_cancel(message: Message, state: FSMContext):
    """Cancel form"""
    await message.answer("Заявка отменена.", reply_markup=get_main_menu_keyboard())
    reset_user_state(message.from_user.id)
    await state.clear()

@router.message(F.text == "❌ Отмена")
async def cancel_any_form(message: Message, state: FSMContext):
    """Cancel any form"""
    await message.answer("Отменено.", reply_markup=get_main_menu_keyboard())
    reset_user_state(message.from_user.id)
    await state.clear()

# ===== BACK BUTTON =====
@router.message(F.text == "⬅️ Назад")
async def back_handler(message: Message, state: FSMContext):
    """Back to main menu"""
    await state.clear()
    await message.answer("Возвращаюсь в главное меню...", reply_markup=get_main_menu_keyboard())

# ===== DEFAULT HANDLER =====
@router.message()
async def echo_handler(message: Message):
    """Handle unknown messages"""
    await message.answer(
        "Я не понял 🤔\n\nВыберите один из вариантов меню выше или введите /help",
        reply_markup=get_main_menu_keyboard()
    )
