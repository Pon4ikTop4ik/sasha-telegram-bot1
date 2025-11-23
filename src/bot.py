import os
from telegram.ext import Application, CommandHandler

print("🎉 Бот запускается на Render!")

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update, context):
    await update.message.reply_text('✅ Бот работает!')

if BOT_TOKEN:
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("🚀 Бот запущен!")
    app.run_polling()
else:
    print("❌ BOT_TOKEN не найден!")
