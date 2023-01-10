from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext
from test import test
from enum import Enum
class State(Enum):
    WAIT = 1
    NAME = 2
    ASC_NAMBER = 3
    NUMBER = 4

master_chat_id = 1605176629

class DATA:
    state = State.WAIT
    count = 0
    set_level = 10
    good_answer = 0
my_data = [DATA, DATA, DATA, DATA, DATA, DATA, DATA, DATA, DATA, DATA]

tempID = [1605176655, 1605176155]

def setIDsesion (id):
    
    for i in range(len(tempID)):
        if id == tempID[i]:
            return i
    tempID.append(id)
    print("New ID")
    return len(tempID)




def messageHandler(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    chat_id = setIDsesion(update.effective_chat.id)
    print(update.effective_chat.id)
    name = update.message.text
    print ("messageHandler" +  update.message.text)
    match my_data[chat_id].state:
        case State.NAME:
            if len(name) > 2:
                my_data[chat_id].state = State.WAIT
                update.message.reply_text("Good")
                update.message.reply_text("After test")
                context.bot.send_message(chat_id=master_chat_id, text="Hello")
                my_data[chat_id].count = 0
                my_data[chat_id].set_level = 10
                my_data[chat_id].good_answer = 0
                choseLevel(update, context)
            else:
                update.message.reply_text("Name is shootly")

        case State.NUMBER:
            if len(name) > 9:
                my_data[chat_id].state = State.WAIT
                update.message.reply_text("Good")
                context.bot.send_message(chat_id=master_chat_id, text=name)
            else:
                update.message.reply_text("Thanks. Good buy")
                return
        case State.WAIT:
            return

def setYourName(update: Update, context: CallbackContext):
    chat_id = setIDsesion(update.effective_chat.id)
    update.message.reply_text("Please write your First name")
    my_data[chat_id].state = State.NAME  

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
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton("YES", callback_data="YES number")], 
                [InlineKeyboardButton("NO", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Do you wont to write number yoyrs fone&")




def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    chatID = setIDsesion(update.effective_chat.id)
    count_up = 0
    print("queryHandler : " + query)
    if "YES number" in query:
        my_data[chatID].state = State.NUMBER
        context.bot.send_message(chat_id=update.effective_chat.id, text="Plese write your phone number")
        return
    
    if "NO good bye" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Good bye")
        return
        
    if "1" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 1
        else:
            if "1" in test[my_data[chatID].set_level][my_data[chatID].count - 1][4]:
                my_data[chatID].good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "2" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 2
        else:
            if "2" in test[my_data[chatID].set_level][my_data[chatID].count - 1][4]:
                my_data[chatID].good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "3" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:  
            my_data[chatID].set_level = 3
        else:
            if "3" in test[my_data[chatID].set_level][my_data[chatID].count - 1][4]:
                my_data[chatID].good_answer += 1
                print(f"Ok")
            else:
                print(f"Bad")

    if "4" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 4


    if "5" in query: 
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 5


    if "6" in query:

        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 6

    if (count_up):
        count_up = 0
        if my_data[chatID].set_level != 0:
            if my_data[chatID].count == 5: #30
                set_number(update, context)
            else:
                A1_level(update, context, my_data[chatID].count, my_data[chatID].set_level)
                print(chatID, my_data[chatID].count)
                my_data[chatID].count = my_data[chatID].count + 1 