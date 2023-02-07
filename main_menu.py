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
def Contacts(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,  text="097-127-19-27 Наталія" )
    context.bot.send_message(chat_id=update.effective_chat.id,  text="natskor2012@gmail.com" )
    context.bot.send_message(chat_id=update.effective_chat.id,  text="Київ, проспект Перемоги 118, офіс 224" )
    context.bot.send_location(chat_id=update.effective_chat.id, latitude = 50.456896, longitude  = 30.377709)


def about(update: Update, context: CallbackContext):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/1.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/2.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/3.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/4.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/5.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/6.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/7.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/8.JPG", "rb"))
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = open("fhoto/9.JPG", "rb"), caption = "Зарпрошуємо на курси англійської та укркаїнської мови, математики, підготовки до школи. \
Ми пропонуємо курси різних напрямів, форматів, тривалості й інтенсивності занять. \
 А у вихідні - розмовний клуб. Практика з носіями мови. \
Зручний графік - ранковий і вечірній час занять. \
Підготовка до міжнародних іспитів. \
Обирайте курс, який підійде саме вам  для досягення ваших цілей.")
    buttons = [[InlineKeyboardButton("Start test, Почати тест", callback_data="Start test")], 
                [InlineKeyboardButton("Finish, закінчити", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Please, choose what you want to do. Будь ласка, виберіть, що ви хочете зробити")


def messageHandler(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    chat_id = setIDsesion(update.effective_chat.id)
    print(update.effective_chat.id)
    name = update.message.text
    print ("messageHandler" +  update.message.text)
    if my_data[chat_id].state == State.NAME:
            if len(name) > 2:
                my_data[chat_id].state = State.WAIT
                update.message.reply_text("Good")
                context.bot.send_message(chat_id=master_chat_id, text="New ID: " + name)
                my_data[chat_id].count = 0
                my_data[chat_id].set_level = 10
                my_data[chat_id].good_answer = 0
                choseLevel(update, context)
            else:
                update.message.reply_text("Name is shootly")

    elif my_data[chat_id].state == State.NUMBER:
            if len(name) > 9:
                my_data[chat_id].state = State.WAIT
                update.message.reply_text("Thanks. Good buy")
                context.bot.send_message(chat_id=master_chat_id, text=name)
                endHandler(update, context)
            else:
                update.message.reply_text("Number  is shootly")
                return
    elif my_data[chat_id].state == State.WAIT:
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
    buttons = [[InlineKeyboardButton("Start testing\r\n Почати тест", callback_data="Start test")], 
                [InlineKeyboardButton("About us\r\n Про нас", callback_data="about")],
                [InlineKeyboardButton("Our contacts and location\r\n Наші контакти та локація", callback_data="location")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Hello " +  first_name)

def choseLevel(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [ [InlineKeyboardButton("Elementary, початковий", callback_data="a")], 
                [InlineKeyboardButton("Pre-Intermediate, нижче середнього", callback_data="b")],  
                [InlineKeyboardButton("Intermediate, середній", callback_data="c")],  
                [InlineKeyboardButton("Upper-Intermediate, вище середнього", callback_data="d")], 
                [InlineKeyboardButton("Advanced, вищій", callback_data="e")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="What level do you want to choose?   Як ви вважаете який у Вас рівень?")
def A1_level(update: Update, context: CallbackContext, count, set_level):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton(test[set_level][count][1], callback_data = str(count) + " a")], 
                [InlineKeyboardButton(test[set_level][count][2], callback_data = str(count)  + " b")], 
                [InlineKeyboardButton(test[set_level][count][3], callback_data = str(count)  + " c")],
                [InlineKeyboardButton(test[set_level][count][4], callback_data = str(count)  + " d")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text=test[set_level][count][0])

def set_number(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    buttons = [[InlineKeyboardButton("YES", callback_data="YES number")], 
                [InlineKeyboardButton("NO", callback_data="NO good bye")]
                ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Do you want us to call you back? Чи бажаете, щоб ми Вам зателефонували?")



def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()
    chatID = setIDsesion(update.effective_chat.id)
    count_up = 0
    print("queryHandler : " + query)
    if "location" in query:
        Contacts(update, context)
        return
    if "YES number" in query:
        my_data[chatID].state = State.NUMBER
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please, write your phone number")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Буль ласка напишить Ваш номер телефону")
        return
    
    if "NO good bye" in query:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You will know you answer through Telegram")
        context.bot.send_message(chat_id=update.effective_chat.id, text="Ви дізнаетесь свої відповіді через Телеграм")
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
            if str(my_data[chatID].count - 1 ) in query:
                if "a" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                    my_data[chatID].good_answer += 1
                    context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                    print(f"Ok")
                else:
                    print(f"Bad")
                    context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
                ls_result[chatID].append([my_data[chatID].count, "a",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])
            else: 
                return
    if "b" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 1
        else:
            if str(my_data[chatID].count - 1 ) in query:
                if "b" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                    my_data[chatID].good_answer += 1
                    context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                    print(f"Ok")
                else:
                    print(f"Bad")
                    context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
                ls_result[chatID].append( [my_data[chatID].count, "b",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])
            else: 
                return
    if "c" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:  
            my_data[chatID].set_level = 2
        else:
            if str(my_data[chatID].count - 1 ) in query:
                if "c" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                    my_data[chatID].good_answer += 1
                    context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                    print(f"Ok")
                else:
                    print(f"Bad")
                    context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
                ls_result[chatID].append([my_data[chatID].count, "c",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])
            else: 
                return
    if "d" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 3
        else:
            if str(my_data[chatID].count - 1 ) in query:
                if "d" in test[my_data[chatID].set_level][my_data[chatID].count - 1][5]:
                    my_data[chatID].good_answer += 1
                    context.bot.send_message(chat_id=update.effective_chat.id, text="✔️")
                    print(f"Ok")
                else:
                    print(f"Bad")
                    context.bot.send_message(chat_id=update.effective_chat.id, text="❎")
                ls_result[chatID].append([ my_data[chatID].count, "d",  test[my_data[chatID].set_level][my_data[chatID].count - 1][5]])
            else:
                return
    if "e" in query:
        count_up = 1
        if my_data[chatID].set_level == 10:
            my_data[chatID].set_level = 4
    if (count_up):
        count_up = 0
        if my_data[chatID].set_level != 10:
            if ((my_data[chatID].set_level == 0) & (my_data[chatID].count == 20)) | \
            ((my_data[chatID].set_level == 1) & (my_data[chatID].count == 30)) | \
            ((my_data[chatID].set_level > 1) & (my_data[chatID].count == 50)):
                set_number(update, context) 
            else:
                print("next")
                A1_level(update, context, my_data[chatID].count, my_data[chatID].set_level)
                print(chatID, my_data[chatID].count)
                print(my_data[chatID].count)
                my_data[chatID].count = my_data[chatID].count + 1 

    #print(ls_result[chatID])


def endHandler(update: Update, context: CallbackContext):
    chatID = setIDsesion(update.effective_chat.id)
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hope to see you in our school!")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Сподіваемось побачити Вас в нашій школі!")
    if my_data[chatID].set_level == 10:
        tempID.pop(chatID)
        return
    if chatID <= (len(ls_result) - 1):
        context.bot.send_message(chat_id=master_chat_id, text="Level : " + str(my_data[chatID].set_level))
        context.bot.send_message(chat_id=master_chat_id, text="ID :" + str(update.effective_chat.id))
        context.bot.send_message(chat_id=master_chat_id, text="RESULT: ")
        context.bot.send_message(chat_id=master_chat_id, text=ls_result[chatID])
        if my_data[chatID].count:
            procent = (my_data[chatID].good_answer * 100) / my_data[chatID].count  
            context.bot.send_message(chat_id=master_chat_id, text="Correct answers: " + str(procent) + "%")
            context.bot.send_message(chat_id=update.effective_chat.id, text="Correct answers: " + str(procent) + "%")
        ls_result[chatID].clear()
        tempID.pop(chatID)
        ls_result.pop(chatID)
        my_data.pop(chatID)


