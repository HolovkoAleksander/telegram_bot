from telegram import Bot, Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, CallbackQueryHandler, Filters
from telegram.utils.request import Request
from main_menu import  queryHandler, messageHandler, setYourName, endHandler, about




#from requests import *
Token_debug = "5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY"
Token = "5839714952:AAFqFuaqLM7BRNJ2CILfdtQe9UaKKHmKmBY"
req=Request(connect_timeout=0.5)
bot=Bot(token=Token,request=req)
updater = Updater(bot=bot, use_context = True)
dispatcher = updater.dispatcher

cmd=[("start","Початок тесту"),("about","Інформація про нас"), ("end","Закінчити тест та отримати результати")]
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






       


dispatcher.add_handler(CommandHandler('start', setYourName))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(CommandHandler('end', endHandler))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))
dispatcher.add_handler(CallbackQueryHandler(queryHandler))

updater.start_polling()
updater.idle()