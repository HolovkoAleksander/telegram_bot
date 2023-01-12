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
my_data = [DATA, DATA, DATA]


result = []
ls_result = [result, result]
tempID = [1605176655, 1605176155]

def setIDsesion (id):
    
    for i in range(len(tempID)):
        if id == tempID[i]:
            return i
    tempID.append(id)
    ls_result.append(result)
    my_data.append(DATA)
    print("New ID")
    return len(tempID)

def about(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto.jpg", "rb"), caption = "У Бразилії евакуювали президента зі столиці через заворушення. Повідомляється, що прихильники колишнього президента країни Жаїра Болсонару увірвалися в урядові будівлі.\
    За даними іноземних видань, одна частина демонстрантів, проникнувши в будівлю національного Конгресу, почала там робити селфі та різні фотознімки.\
    Інша ж група людей почала штурмувати резиденцію президента. Водночас місцева влада вже віддала наказ ввести військових у столицю Бразилії, щоб заспокоїти громадян.\
    Відомо, що самого президента Бразилії тимчасово евакуювали з міста через дії демонстрантів. Луїс Інасіо Лула да Сілва зараз перебуває в Сан-Паулу, зазначають закордонні журналісти.")
    buttons = [[InlineKeyboardButton("Start test", callback_data="Start test")], 
                [InlineKeyboardButton("end", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Please chouse what do you wont to do")


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
                context.bot.send_message(chat_id=master_chat_id, text="New ID: " + name)
                my_data[chat_id].count = 0
                my_data[chat_id].set_level = 10
                my_data[chat_id].good_answer = 0
                choseLevel(update, context)
            else:
                update.message.reply_text("Name is shootly")

        case State.NUMBER:
            if len(name) > 9:
                my_data[chat_id].state = State.WAIT
                update.message.reply_text("Thanks. Good buy")
                context.bot.send_message(chat_id=master_chat_id, text=name)
                endHandler(update, context)
            else:
                update.message.reply_text("Number  is shootly")
                return
        case State.WAIT:
            return

def setYourName(update: Update, context: CallbackContext):
    chat_id = setIDsesion(update.effective_chat.id)
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    context.bot.send_message(chat_id=master_chat_id, text="New ID: " + str(chat_id))
    context.bot.send_message(chat_id=master_chat_id, text= first_name + last_name)
    context.bot.send_message(chat_id=master_chat_id, text= username)
    update.message.reply_text("Hello " +  first_name)
    buttons = [[InlineKeyboardButton("Start test", callback_data="Start test")], 
                [InlineKeyboardButton("About as", callback_data="about")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Please chouse what do you wont to do")

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
    buttons = [[InlineKeyboardButton("YES, and we will col to you", callback_data="YES number")], 
                [InlineKeyboardButton("NO, I wont to ask from telegram", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Do you wont to write number yours fone?")




def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    chatID = setIDsesion(update.effective_chat.id)
    count_up = 0
    print("queryHandler : " + query)
    if "YES number" in query:
        my_data[chatID].state = State.NUMBER
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please write your phone number")
        return
    
    if "NO good bye" in query:
        endHandler(update, context)
        return

    if "Start test" in query:
        my_data[chatID].state = State.WAIT
        my_data[chatID].count = 0
        my_data[chatID].set_level = 10
        my_data[chatID].good_answer = 0
        choseLevel(update, context)
        return

    if "about" in query:
        about(update, context)
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
            ls_result[chatID].append(("1",  test[my_data[chatID].set_level][my_data[chatID].count - 1][4]))

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
            ls_result[chatID].append(("2",  test[my_data[chatID].set_level][my_data[chatID].count - 1][4]))

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
            ls_result[chatID].append(("3",  test[my_data[chatID].set_level][my_data[chatID].count - 1][4]))

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


def endHandler(update: Update, context: CallbackContext):
    chatID = setIDsesion(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for your attention!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Good bye")

    if chatID <= (len(ls_result) - 1):
        context.bot.send_message(chat_id=master_chat_id, text="Level :")
        context.bot.send_message(chat_id=master_chat_id, text=my_data[chatID].set_level)
        context.bot.send_message(chat_id=master_chat_id, text="ID :")
        context.bot.send_message(chat_id=master_chat_id, text=update.effective_chat.id)
        context.bot.send_message(chat_id=master_chat_id, text="RESULT: ")
        context.bot.send_message(chat_id=master_chat_id, text=ls_result[chatID])

        ls_result[chatID].clear()
        tempID.pop(chatID)
        ls_result.pop(chatID)
        my_data.pop(chatID)


