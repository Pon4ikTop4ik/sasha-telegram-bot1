
import os
from telegram.ext import Application, CommandHandler

print("🚀 Бот запускается...")

BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ ОШИБКА: BOT_TOKEN не установлен!")
    print("💡 Добавь BOT_TOKEN в Railway Variables")
else:
    print("✅ Токен найден, запускаем бота...")

async def start(update, context):
    await update.message.reply_text('🎉 Бот работает на Railway!')

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🔧 Используем polling...")
app.run_polling()
