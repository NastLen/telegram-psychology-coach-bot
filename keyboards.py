"""
Keyboards for the bot
"""
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BTN_ABOUT, BTN_SERVICES, BTN_FAQ, BTN_CONTACT, BTN_BOOK, BTN_LEAD_FORM,
    BTN_BOOK_LINK, BTN_WEBSITE, BTN_WHATSAPP, BTN_EMAIL, BTN_ASK_QUESTION,
    BTN_BACK, BTN_SUBMIT_FORM, BTN_CANCEL
)

# Main menu keyboard
def get_main_menu_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=BTN_ABOUT), KeyboardButton(text=BTN_SERVICES)],
            [KeyboardButton(text=BTN_FAQ), KeyboardButton(text=BTN_CONTACT)],
            [KeyboardButton(text=BTN_BOOK), KeyboardButton(text=BTN_LEAD_FORM)],
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )

# Back button
def get_back_button():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=BTN_BACK)]],
        resize_keyboard=True
    )

# Booking options inline keyboard
def get_booking_inline_keyboard(booking_url, website_url, calendly_url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BTN_BOOK_LINK, url=booking_url)],
            [InlineKeyboardButton(text=BTN_WEBSITE, url=website_url)],
        ]
    )

# Contact options inline keyboard
def get_contact_inline_keyboard(whatsapp_url, email):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BTN_WHATSAPP, url=whatsapp_url)],
            [InlineKeyboardButton(text=BTN_EMAIL, url=f"mailto:{email}")],
            [InlineKeyboardButton(text=BTN_ASK_QUESTION, callback_data="ask_question")],
        ]
    )

# Question form cancel keyboard
def get_question_cancel_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=BTN_CANCEL)]],
        resize_keyboard=True
    )

# Services submenu inline keyboard
def get_services_inline_keyboard(booking_url, pricing_url):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=BTN_BOOK_LINK, url=booking_url)],
            [InlineKeyboardButton(text="💳 View Pricing", url=pricing_url)],
        ]
    )
