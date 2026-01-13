# 🎯 BOT FLOW DIAGRAMS

## Main Menu Navigation

```
                          /start or /help
                              ↓
                    ┌─────────────────────┐
                    │   MAIN MENU (6)     │
                    │                     │
                    │  [ℹ️ About]         │
                    │  [💼 Services]      │
                    │  [❓ FAQ]           │
                    │  [📞 Contact]       │
                    │  [📅 Book Now]      │
                    │  [📝 Leave Request] │
                    └─────────────────────┘
                              ↑
                    [⬅️ Back] (all screens)
```

---

## Feature: About

```
User: [ℹ️ About]
  ↓
Bot: Shows ABOUT_TEXT
  • Who I am
  • My approach
  • Experience
  • Main themes
  • Languages
  ↓
Main Menu appears again
```

---

## Feature: Services

```
User: [💼 Services]
  ↓
Bot: Shows SERVICES_TEXT with inline buttons
  • Single session
  • Package (4 sessions)
  • Online/Offline
  • Price info
  ↓
Inline Buttons:
  [📅 Open Calendar] → BOOKING_URL
  [💳 View Pricing] → PAYMENT_URL
```

---

## Feature: Contact

```
User: [📞 Contact]
  ↓
Bot: Shows CONTACT_TEXT with 3 options
  ↓
  ├─→ [💬 WhatsApp] → WHATSAPP_URL (direct link)
  ├─→ [📧 Write Email] → mailto:EMAIL
  └─→ [❓ Ask a Question] → START FORM
        ↓
        Bot: "Write your question"
        User: Sends text
        ↓
        Admin Chat: Question forwarded to you
        Bot to User: "✅ Thanks! We'll respond soon"
        ↓
        You: Can reply directly to user
```

---

## Feature: Book Now

```
User: [📅 Book Now]
  ↓
Bot: Shows inline button
  ↓
  [📅 Open Calendar]
  ↓
  Opens BOOKING_URL (Calendly/booking page)
  ↓
  User books + pays on external site
  ✓ Done
```

---

## Feature: Lead Form (Multi-step)

```
User: [📝 Leave a Request]
  ↓
State: LeadForm.asking_name
Bot: "📝 Please enter your name"
User: Types name (e.g., "John")
  ↓
State: LeadForm.asking_contact
Bot: "How to contact you?" (email/phone/telegram)
User: Types contact (e.g., "john@email.com")
  ↓
State: LeadForm.asking_request
Bot: "Brief description of your request"
User: Types request
  ↓
State: LeadForm.confirming
Bot: Shows summary with [✅ Yes] [❌ Отмена]

  If [✅ Yes]:
    ↓
    Admin Chat: Form data sent to you
    Bot to User: "✅ Form sent! We'll contact you"
    ↓
    State: CLEARED (back to main menu)

  If [❌ Отмена]:
    ↓
    Bot: "Cancelled"
    ↓
    Back to Main Menu
```

---

## Feature: FAQ

```
User: [❓ FAQ]
  ↓
Bot: Shows FAQ_TEXT
  • How does it work?
    1. Book appointment
    2. Receive link
    3. Meet & discuss
    4. Get notes/recommendations

  • How to prepare?
    • Relax, no preparation needed
    • Can prepare questions
    • Comfortable environment

  • Cancellation policy
    • 48h before = free cancellation
    • < 48h = session charged
    • Force majeure discussed individually

  • Languages
    • 🇷🇺 Russian
    • 🇬🇧 English
    • Can mix languages
  ↓
Main Menu appears
```

---

## Admin Notification Flow

### When User Asks Question:

```
User sends question → Bot receives
  ↓
Admin Chat (you) receives:
┌────────────────────────────────┐
│ ❓ New Question                │
│                                │
│ User ID: 123456789            │
│ Name: John                     │
│ Question: How does it work?    │
└────────────────────────────────┘
  ↓
You can reply directly to that user
```

### When User Submits Form:

```
User fills form → Confirms
  ↓
Admin Chat (you) receives:
┌────────────────────────────────┐
│ 📋 New Lead                    │
│                                │
│ Telegram ID: 123456789        │
│ Name: John Smith               │
│ Contact: john@email.com       │
│ Request: I need help with... │
└────────────────────────────────┘
  ↓
You can contact user directly
```

---

## Complete User Journey - Example

```
Day 1: Discovery
  ├─ User finds bot link
  ├─ /start → Main Menu
  ├─ Reads [ℹ️ About]
  ├─ Checks [💼 Services]
  ├─ Reads [❓ FAQ]
  └─ Checks [📞 Contact]

Day 1-2: Decision
  ├─ User clicks [💬 WhatsApp]
  ├─ Chats with you on WhatsApp
  └─ Gets questions answered

Day 2: Booking
  ├─ User returns to bot
  ├─ Taps [📅 Book Now]
  ├─ Opens Calendly
  ├─ Selects time slot
  ├─ Pays on your website
  └─ Receives confirmation

Day 2 (Alternative):
  ├─ User fills [📝 Leave a Request]
  ├─ You receive form in Telegram
  ├─ You reply directly to user
  ├─ User books & pays
  └─ ✓ Session confirmed
```

---

## Data Flow

```
┌─────────────────────────────────┐
│     User (Telegram)             │
└──────────────┬──────────────────┘
               │
               ↓ (messages)
┌─────────────────────────────────┐
│    Telegram API                 │
└──────────────┬──────────────────┘
               │
               ↓
┌─────────────────────────────────┐
│    Bot (main.py)                │
│  • Receives messages            │
│  • Processes handlers           │
│  • Manages state (FSM)          │
└──────────────┬──────────────────┘
               │
        ┌──────┴──────┐
        ↓             ↓
┌──────────────┐  ┌─────────────────┐
│ User State   │  │ External Links  │
│ (memory)     │  │ • Calendly      │
│              │  │ • Website       │
│ Form data:   │  │ • Email         │
│ • Name       │  │ • WhatsApp      │
│ • Contact    │  └─────────────────┘
│ • Request    │
└──────────────┘

        ↓ (admin notifications)
┌─────────────────────────────────┐
│    YOUR TELEGRAM ADMIN CHAT      │
│  • Forms                         │
│  • Questions                     │
│  • You can reply directly        │
└─────────────────────────────────┘
```

---

## State Machine (FSM) Diagram

```
Question Form:
┌──────────────┐
│   IDLE       │
└──────┬───────┘
       │ /ask_question clicked
       ↓
┌──────────────────────────┐
│ asking_question          │
│ Bot: "Write question"    │
└──────┬────────────────────┘
       │ User sends text
       ↓
      [Question sent to admin]
       ↓ [CLEARED]
┌──────────────┐
│   IDLE       │
└──────────────┘

Lead Form:
┌──────────────┐
│   IDLE       │
└──────┬───────┘
       │ Leave Request clicked
       ↓
┌──────────────────────────┐
│ asking_name              │
│ Bot: "Your name?"        │
└──────┬────────────────────┘
       │ User sends name
       ↓
┌──────────────────────────┐
│ asking_contact           │
│ Bot: "How to contact?"   │
└──────┬────────────────────┘
       │ User sends contact
       ↓
┌──────────────────────────┐
│ asking_request           │
│ Bot: "What's your req?"  │
└──────┬────────────────────┘
       │ User sends request
       ↓
┌──────────────────────────────┐
│ confirming                   │
│ Bot: Show summary + confirm  │
└──────┬─────────────┬──────────┘
       │ [Yes]       │ [Cancel]
       ↓             ↓
   [Send to admin]   [CLEARED]
       ↓             ↓
    [CLEARED]    ┌──────────────┐
       ↓         │   IDLE       │
┌──────────────┐ └──────────────┘
│   IDLE       │
└──────────────┘
```

---

## Button Layout Visualization

### Main Menu (Reply Keyboard)

```
┌─────────────────────────────────┐
│                                 │
│  ┌──────────────┐ ┌──────────┐ │
│  │ ℹ️ About    │ │ 💼 Srvcs │ │
│  └──────────────┘ └──────────┘ │
│                                 │
│  ┌──────────────┐ ┌──────────┐ │
│  │ ❓ FAQ       │ │ 📞 Contact
│  │              │ │          │ │
│  └──────────────┘ └──────────┘ │
│                                 │
│  ┌──────────────┐ ┌──────────┐ │
│  │ 📅 Book Now  │ │ 📝 Leave │ │
│  └──────────────┘ └──────────┘ │
│                                 │
└─────────────────────────────────┘
```

### Services (Inline Keyboard)

```
Message with buttons:
"📋 Formats of work..."

┌──────────────────────────┐
│ 📅 Open Calendar        │ → https://calendly.com/...
└──────────────────────────┘

┌──────────────────────────┐
│ 💳 View Pricing         │ → https://your-site.com/pricing
└──────────────────────────┘
```

### Contact (Inline Keyboard)

```
Message with buttons:
"📞 Contact me..."

┌──────────────────────────┐
│ 💬 WhatsApp             │ → https://wa.me/...
└──────────────────────────┘

┌──────────────────────────┐
│ 📧 Write Email          │ → mailto:email@...
└──────────────────────────┘

┌──────────────────────────┐
│ ❓ Ask a Question       │ → Start form
└──────────────────────────┘
```

---

## Deployment Architecture

```
┌─────────────────────────────────────────┐
│         Your Server/Cloud               │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │     Python Bot Application       │  │
│  │  • main.py (entry point)         │  │
│  │  • handlers.py (logic)           │  │
│  │  • config.py (settings)          │  │
│  │  • keyboards.py (UI)             │  │
│  │  • database.py (state)           │  │
│  │                                  │  │
│  │  ↕ asyncio polling               │  │
│  └──────────────────────────────────┘  │
└─────────────────────────────────────────┘
         │
         │ (HTTPS polling)
         │
┌─────────────────────────────────────────┐
│     Telegram Bot API Servers            │
│     (Telegram manages this)             │
└─────────────────────────────────────────┘
         │
         │ (Telegram protocol)
         │
┌─────────────────────────────────────────┐
│     User's Telegram Client              │
│     (Mobile app / Desktop / Web)        │
└─────────────────────────────────────────┘
```

---

**All flows are automated and user-friendly! 🎉**
