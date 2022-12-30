from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext

def choseLevel(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton("A1_Beginner", callback_data="A1")], 
                [InlineKeyboardButton("A2_Elementary", callback_data="A2")], 
                [InlineKeyboardButton("B1_Intermediate", callback_data="B1")],  
                [InlineKeyboardButton("B2_Upper-Intermediate", callback_data="B2")], 
                [InlineKeyboardButton("C1_Advanced", callback_data="C1")], 
                [InlineKeyboardButton("C2_Proficiency", callback_data="C2")] ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="What do you think is your level of English?")


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    if "A1" in query:
        print(f"A1")

    if "A2" in query:
        print(f"A2")

    if "B1" in query:
        print(f"B1")    
    if "B2" in query:
        print(f"B2")

    if "C1" in query:
        print(f"C1")   

    if "C2" in query:
        print(f"C2")