import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# /start কমান্ডের রিপ্লাই
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("online ✅")

# জয়েন এবং লিফট মেসেজ ডিলিট করার ফাংশন
async def delete_service_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")

def main():
    # আপনার বট টোকেন এখানে দিন বা এনভায়রনমেন্ট ভ্যারিয়েবল হিসেবে সেট করুন
    TOKEN = os.getenv("BOT_TOKEN")
    
    application = Application.builder().token(TOKEN).build()

    # কমান্ড হ্যান্ডলার
    application.add_handler(CommandHandler("start", start))

    # সার্ভিস মেসেজ (নতুন মেম্বার আসা বা চলে যাওয়া) ফিল্টার
    service_message_filter = filters.StatusUpdate.NEW_CHAT_MEMBERS | filters.StatusUpdate.LEFT_CHAT_MEMBER
    application.add_handler(MessageHandler(service_message_filter, delete_service_messages))

    # বট রান করা
    application.run_polling()

if __name__ == "__main__":
    main()
