from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

# Токен бота
TOKEN = '7908023640:AAHfy4Ve_744A4ueLvN_7VP-cKfc2IkuZEQ'

# Функция для команды /start
async def start(update: Update, context):
    keyboard = [
        [KeyboardButton("🌊 ATLANTIDA 🌊", web_app=WebAppInfo(url="https://yourname.github.io/atlantida-web-app"))],
        [KeyboardButton("ℹ️ FAQ"), KeyboardButton("📧 Поддержка")],
        [KeyboardButton("🏛️ Канал"), KeyboardButton("💰 ОПТ")]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "Добро пожаловать в магазин ATLANTIDA! Выберите действие:",
        reply_markup=reply_markup
    )

# Команда для открытия магазина (Web App)
async def store(update: Update, context):
    await update.message.reply_text("Открыть магазин: [Перейти](https://yourname.github.io/atlantida-web-app)", parse_mode='Markdown')

# Команда для FAQ
async def faq(update: Update, context):
    await update.message.reply_text("Часто задаваемые вопросы:\n1. Как заказать?\n2. Как оплатить?\n3. Какой срок доставки?")

# Команда для поддержки
async def support(update: Update, context):
    await update.message.reply_text("Контакты администраторов:\nEmail: support@yourstore.com\nTelegram: @admin_support")

# Команда для канала
async def channel(update: Update, context):
    await update.message.reply_text("Присоединяйтесь к нашему каналу: [Канал магазина](https://t.me/yourchannel)")

# Команда для оптовых клиентов
async def opt(update: Update, context):
    await update.message.reply_text("Заказы оптом:\nПрайс: [Скачать](https://yourstore.com/price)\nКонтакты для опта: @opt_manager")

# Функция обработки сообщений с кнопками
async def handle_message(update: Update, context):
    text = update.message.text
    if text == '🌊 ATLANTIDA 🌊':
        await store(update, context)
    elif text == 'ℹ️ FAQ':
        await faq(update, context)
    elif text == '📧 Поддержка':
        await support(update, context)
    elif text == '🏛️ Канал':
        await channel(update, context)
    elif text == '💰 ОПТ':
        await opt(update, context)
    else:
        await update.message.reply_text("Неизвестная команда. Попробуйте еще раз.")

# Обработка данных, полученных из Web App
async def handle_web_app_data(update: Update, context):
    data = update.message.web_app_data.data  # Получение данных от Web App
    await update.message.reply_text(f"Получены данные из Web App: {data}")

if __name__ == '__main__':
    # Создание приложения
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработка команды /start
    app.add_handler(CommandHandler('start', start))

    # Обработка сообщений с кнопками
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Обработка данных от Web App
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))

    # Запуск бота
    app.run_polling()
