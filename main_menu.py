from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
from test import test
from enum import Enum
class State(Enum):
    WAIT = 1
    NAME = 2
    ASC_NAMBER = 3
    NUMBER = 4
state = State.WAIT
master_chat_id = 1605176629

def messageHandler(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    global master_chat_id, state
    print(update.effective_chat.id)
    name = update.message.text
    print ( update.message.text)
    match state:
        case State.NAME:
            if len(name) > 2:
                state = State.WAIT
                update.message.reply_text("Good")
                update.message.reply_text("After test")
                context.bot.send_message(chat_id=master_chat_id, text="Hello")
                choseLevel(update, context)
            else:
                update.message.reply_text("Name is shootly")

        case State.NUMBER:
            if len(name) > 9:
                state = State.WAIT
                update.message.reply_text("Good")
                context.bot.send_message(chat_id=master_chat_id, text=name)
            else:
                update.message.reply_text("Thanks. Good buy")
                return
        case State.WAIT:
            return

def setYourName(update: Update, context: CallbackContext):
    global state
    update.message.reply_text("Please write your First name")
    state = State.NAME  

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

def set_number(update: Update, context: CallbackContext):
    global state
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton("YES", callback_data="YES number")], 
                [InlineKeyboardButton("NO", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Do you wont to write number yoyrs fone&")


count = 0
set_level = 10
good_answer = 0

def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    global count, set_level, good_answer, state
    print(query)
    if "YES number" in query:
        state = State.NUMBER
        context.bot.send_message("Plese write your phone number")
    
    if "NO good bye" in query:
        context.bot.send_message("Good bye")
        return
    if "1" in query:
        count_up = 1
        if set_level == 10:
            set_level = 1
        else:
            if "1" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "2" in query:
        count_up = 1
        if set_level == 10:
            set_level = 2
        else:
            if "2" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "3" in query:
        count_up = 1
        if set_level == 10:  
            set_level = 3
        else:
            if "3" in test[set_level][count - 1][4]:
                good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "4" in query:
        count_up = 1
        if set_level == 10:
            set_level = 4


    if "5" in query: 
        count_up = 1
        if set_level == 10:
            set_level = 5


    if "6" in query:

        count_up = 1
        if set_level == 10:
            set_level = 6

    if (count_up):
        count_up = 0
        if set_level != 0:
            if count == 5: #30
                set_number(update, context)
            else:
                A1_level(update, context, count, set_level)
                print(count)
                count = count + 1 