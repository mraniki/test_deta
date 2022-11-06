from fastapi import FastAPI, Request
from telegram import Update, Bot,InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Dispatcher, CommandHandler, CallbackContext, MessageHandler, Filters,CallbackQueryHandler

BotToken = "mytoken"

def start(update: Update, _: CallbackContext):
    update.message.reply_text("hiiii , how you doin!?")


def get_dispatcher():
    bot = Bot(BotToken)
    dispatcher = Dispatcher(bot=bot, update_queue=None, use_context=True)
    dispatcher.add_handler(CommandHandler('start', start))
    return dispatcher

dispatcher = get_dispatcher()

app = FastAPI()

@app.post("/webhook")
async def webhook_handler(req: Request):
    data = await req.json()
    update = Update.de_json(data, dispatcher.bot)
    dispatcher.process_update(update)
				