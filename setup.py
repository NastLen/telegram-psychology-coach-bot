#!/usr/bin/env python3
"""
Interactive setup script for the Telegram bot
Run: python setup.py
"""
import os
import sys

def main():
    print("=" * 60)
    print("🤖 Telegram Coach Bot - Initial Setup")
    print("=" * 60)
    print()
    
    # Check if config.py already has ADMIN_CHAT_ID set
    config_file = "config.py"
    
    print("📋 Let's configure your bot!\n")
    
    # 1. Bot Token
    print("✅ Bot Token already set in config.py")
    print("   Token: 8538542036:AAEOnFstif9BBcfoSYV4DK0i_icM4Sw6Tqs\n")
    
    # 2. Admin Chat ID
    print("📌 Next, set your Admin Chat ID")
    print("   To find it:")
    print("   1. Send a message to @userinfobot in Telegram")
    print("   2. It will show your User ID\n")
    
    admin_id = input("Enter your Admin Chat ID (or press Enter to skip): ").strip()
    
    # 3. External URLs
    print("\n📍 External Links\n")
    
    booking_url = input("Booking URL (Calendly, etc) [https://calendly.com/your-coach]: ").strip()
    if not booking_url:
        booking_url = "https://calendly.com/your-coach"
    
    website_url = input("Website URL [https://your-website.com]: ").strip()
    if not website_url:
        website_url = "https://your-website.com"
    
    payment_url = input("Payment/Pricing URL [https://your-website.com/pricing]: ").strip()
    if not payment_url:
        payment_url = "https://your-website.com/pricing"
    
    whatsapp_url = input("WhatsApp URL [https://wa.me/+49XXXXXXXXXX]: ").strip()
    if not whatsapp_url:
        whatsapp_url = "https://wa.me/+49XXXXXXXXXX"
    
    email = input("Email address [your@email.com]: ").strip()
    if not email:
        email = "your@email.com"
    
    # 4. Update config.py
    print("\n💾 Updating config.py...\n")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Admin ID
    if admin_id:
        content = content.replace('ADMIN_CHAT_ID = None', f'ADMIN_CHAT_ID = {admin_id}')
    
    # Update URLs
    content = content.replace(
        'BOOKING_URL = "https://calendly.com/your-coach"',
        f'BOOKING_URL = "{booking_url}"'
    )
    content = content.replace(
        'WEBSITE_URL = "https://your-website.com"',
        f'WEBSITE_URL = "{website_url}"'
    )
    content = content.replace(
        'PAYMENT_URL = "https://your-website.com/pricing"',
        f'PAYMENT_URL = "{payment_url}"'
    )
    content = content.replace(
        'WHATSAPP_URL = "https://wa.me/+49XXXXXXXXXX"',
        f'WHATSAPP_URL = "{whatsapp_url}"'
    )
    content = content.replace(
        'EMAIL = "your.email@example.com"',
        f'EMAIL = "{email}"'
    )
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Configuration saved!")
    print("\n" + "=" * 60)
    print("🎉 Setup complete!\n")
    print("Next steps:")
    print("1. Edit ABOUT_TEXT, SERVICES_TEXT, FAQ_TEXT in config.py")
    print("   (fill in your actual bio, services, etc.)\n")
    print("2. Install dependencies:")
    print("   pip install -r requirements.txt\n")
    print("3. Run the bot:")
    print("   python main.py\n")
    print("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
