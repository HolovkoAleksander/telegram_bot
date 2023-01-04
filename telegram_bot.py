from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler, Filters
from telegram.utils.request import Request
from main_menu import choseLevel, queryHandler
master_chat_id = 1605176629

#from requests import *
Token = "5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY"
req=Request(connect_timeout=0.5)
bot=Bot(token=Token,request=req)
updater = Updater(bot=bot, use_context = True)
dispatcher = updater.dispatcher

cmd=[("start","Press to start testing"),("end","Press to end testing")]
bot.set_my_commands(cmd)

def help(update, context):
    update.message.reply_text(
        """
        /start -> 
        /help ->
        /context -> 
        /Python ->
        /SQL
        """
        )

#def startCommand(update: Update, context: CallbackContext):
#    buttons = [ [KeyboardButton("Start")], 
 #               [KeyboardButton("End")]]
 #   context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardMarkup(buttons))

def content(update, context):
    update.message.reply_text("Welcome")

def Python(update, context):
    update.message.reply_text("Welcome : https://www.youtube.com/watch?v=sO42syEV4sY&ab_channel=MarkSolonin")

allowedUsernames = []



def messageHandler(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    global master_chat_id
    print(update.effective_chat.id)
    name = update.message.text
    if len(name) > 2:
        print (update.message.text)
        update.message.reply_text("Good")
        update.message.reply_text("After test")
        context.bot.send_message(chat_id=master_chat_id, text="Hello")
        choseLevel(update, context)
    else:
        update.message.reply_text("Name is shootly")

def setYourName(update: Update, context: CallbackContext):
     update.message.reply_text("Please write your First name")
    
        


dispatcher.add_handler(CommandHandler('start', setYourName))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()
updater.idle()