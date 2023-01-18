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
    def __init__(self, state, count, set_level, good_answer):
        self.state = state
        self.count = count
        self.set_level = set_level
        self.good_answer = good_answer
#class RESULT:
#    def __init__(self, count, answer, corret_answer):
#        self.count = count
#        self.answer = answer
#        self.corret_answer = corret_answer
my_data = []


ls_result = []
tempID = []

def setIDsesion (id):
    if len(tempID):
        for i in range(len(tempID)):
            if id == tempID[i]:
                return i
    tempID.append(id)
    ls_result.append([])
    my_data.append(DATA(State.WAIT, 0, 10 , 0))
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
    if first_name:
        if last_name:
            context.bot.send_message(chat_id=master_chat_id, text=first_name +"/"+ last_name)
        else:
            context.bot.send_message(chat_id=master_chat_id, text=first_name)
    if username:
        context.bot.send_message(chat_id=master_chat_id, text="Username: " + username)
    update.message.reply_text("Hello " +  first_name)
    buttons = [[InlineKeyboardButton("Start test", callback_data="Start test")], 
                [InlineKeyboardButton("About as", callback_data="about")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Please chouse what do you wont to do")

def choseLevel(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [ [InlineKeyboardButton("Elementary", callback_data="a")], 
                [InlineKeyboardButton("Intermediate", callback_data="b")],  
                [InlineKeyboardButton("Upper-Intermediate", callback_data="c")], 
                [InlineKeyboardButton("Advanced", callback_data="d")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="What do you think is your level of English?")

def A1_level(update: Update, context: CallbackContext, count, set_level):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton(test[set_level][count][1], callback_data="a")], 
                [InlineKeyboardButton(test[set_level][count][2], callback_data="b")], 
                [InlineKeyboardButton(test[set_level][count][3], callback_data="c")],
                [InlineKeyboardButton(test[set_level][count][4], callback_data="d")]]
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

    if "a" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 0
        else:
            if "a" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                my_data[chatID].good_answer += 1
                context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                print(f"Ok")
            else:
                print(f"Bad")
                context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
            ls_result[chatID].append([my_data[chatID].count, "a",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])

    if "b" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 1
        else:
            if "b" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                my_data[chatID].good_answer += 1
                context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                print(f"Ok")
            else:
                print(f"Bad")
                context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
            ls_result[chatID].append( [my_data[chatID].count, "b",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])

    if "c" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:  
            my_data[chatID].set_level = 2
        else:
            if "c" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                my_data[chatID].good_answer += 1
                context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                print(f"Ok")
            else:
                print(f"Bad")
                context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
            ls_result[chatID].append([my_data[chatID].count, "c",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])

    if "d" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 3
        else:
            if "d" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                my_data[chatID].good_answer += 1
                context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                print(f"Ok")
            else:
                print(f"Bad")
                context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
            ls_result[chatID].append([ my_data[chatID].count, "d",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])

    if (count_up):
        count_up = 0
        if my_data[chatID].set_level != 10:
            if my_data[chatID].count == 50:
                procent = (my_data[chatID].good_answer * 100) / my_data[chatID].count  
                context.bot.send_message(chat_id=update.effective_chat.id, text="Good answer: " + str(procent) + "%")
                set_number(update, context) 
            else:
                A1_level(update, context, my_data[chatID].count, my_data[chatID].set_level)
                print(chatID, my_data[chatID].count)
                print(my_data[chatID].count)
                my_data[chatID].count = my_data[chatID].count + 1 

    #print(ls_result[chatID])


def endHandler(update: Update, context: CallbackContext):
    chatID = setIDsesion(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thanks for your attention!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Good bye")

    if chatID <= (len(ls_result) - 1):
        context.bot.send_message(chat_id=master_chat_id, text="Level : " + str(my_data[chatID].set_level))
        context.bot.send_message(chat_id=master_chat_id, text="ID :" + str(update.effective_chat.id))
        context.bot.send_message(chat_id=master_chat_id, text="RESULT: ")
        context.bot.send_message(chat_id=master_chat_id, text=ls_result[chatID])
        if my_data[chatID].count:
            procent = (my_data[chatID].good_answer * 100) / my_data[chatID].count  
            context.bot.send_message(chat_id=master_chat_id, text="Good answer: " + str(procent) + "%")
        ls_result[chatID].clear()
        tempID.pop(chatID)
        ls_result.pop(chatID)
        my_data.pop(chatID)


