from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

current_mode = None

# Створення кнопок
async def send_main_menu(update: Update, text: str):
    keyboard = [['menu', 'whisper', 'scream']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(text, reply_markup=reply_markup)

# Початок
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_main_menu(update, "Виберіть команду:")

# Кнопка /menu
async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await send_main_menu(update, "Команди:\n- whisper: перетворення тексту на маленькі літери.\n- scream: перетворення тексту на великі літери.")

# Кнопки /whisper та /scream
async def handle_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_mode
    command = update.message.text

    if command == 'whisper':
        current_mode = 'whisper'
        await update.message.reply_text("Режим Whisper: Введіть текст.")
    elif command == 'scream':
        current_mode = 'scream'
        await update.message.reply_text("Режим Scream: Введіть текст.")

# Перетворення тексту
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_mode
    usertext = update.message.text

    if current_mode == 'whisper':
        response = usertext.lower()
    elif current_mode == 'scream':
        response = usertext.upper()
    else:
        response = "Оберіть whisper або scream."

    await send_main_menu(update, response)
    current_mode = None



if __name__ == '__main__':
    token = 'Токен боту'

    application = ApplicationBuilder().token(token).build()

    # Відстежування команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.Regex('^menu$'), menu))
    application.add_handler(MessageHandler(filters.Regex('^(whisper|scream)$'), handle_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    # Запуск бота
    application.run_polling()

