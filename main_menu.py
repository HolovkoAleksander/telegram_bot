from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
from test import test


  

def choseLevel(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton("A1_Beginner", callback_data="1")], 
                [InlineKeyboardButton("A2_Elementary", callback_data="2")], 
                [InlineKeyboardButton("B1_Intermediate", callback_data="3")],  
                [InlineKeyboardButton("B2_Upper-Intermediate", callback_data="4")], 
                [InlineKeyboardButton("C1_Advanced", callback_data="5")], 
                [InlineKeyboardButton("C2_Proficiency", callback_data="6")] ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="What do you think is your level of English?")

def A1_level(update: Update, context: CallbackContext, count, set_level):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton(test[set_level][count][1], callback_data="1")], 
                [InlineKeyboardButton(test[set_level][count][2], callback_data="2")], 
                [InlineKeyboardButton(test[set_level][count][3], callback_data="3")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text=test[set_level][count][0])

count = 0
set_level = 10
good_answer = 0

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global count, set_level, good_answer
    if "1" in query:
        print(f"A1")
        if set_level == 10:
            set_level = 1
        else:
            if "1" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "2" in query:
        print(f"A2")
        if set_level == 10:
            set_level = 2
        else:
            if "2" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "3" in query:
        print(f"B1")  
        if set_level == 10:  
            set_level = 3
        else:
            if "3" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "4" in query:
        print(f"B2")
        if set_level == 10:
            set_level = 4


    if "5" in query:
        print(f"C1")   
        if set_level == 10:
            set_level = 5


    if "6" in query:
        print(f"C2")
        if set_level == 10:
            set_level = 6

    if set_level != 0:
        A1_level(update, context, count, set_level)
        print(count)
        count = count + 1 