
import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Бот работает!")

async def main():
    token = os.environ["TELEGRAM_TOKEN"]
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
