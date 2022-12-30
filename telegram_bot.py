from telegram import *
from telegram.ext import * 
#from requests import *
Token = "5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY"
updater = Updater("5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY", use_context = True)
dispatcher = updater.dispatcher


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

def startCommand(update: Update, context: CallbackContext):
    buttons = [ [KeyboardButton("A1 Beginner")], 
                [KeyboardButton("A2 Elementary")], 
                [KeyboardButton("B1 Intermediate")],  
                [KeyboardButton("B2 Upper-Intermediate")], 
                [KeyboardButton("C1 Advanced")], 
                [KeyboardButton("C2 Proficiency")] ]
    context.bot.send_message(chat_id=update.effective_chat.id, text="What do you think is your level of English?", reply_markup=ReplyKeyboardMarkup(buttons))

def content(update, context):
    update.message.reply_text("Welcome")

def Python(update, context):
    update.message.reply_text("Welcome : https://www.youtube.com/watch?v=sO42syEV4sY&ab_channel=MarkSolonin")

allowedUsernames = []
def messageHandler(update: Update, context: CallbackContext):
   # if update.effective_chat.username not in allowedUsernames:
   #     context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
   #     return
    if "start" in update.message.text:
        update.message.reply_text("Welcome : https://www.youtube.com/watch?v=sO42syEV4sY&ab_channel=MarkSolonin")
    if "end" in update.message.text:
        update.message.reply_text("Welcome")

    buttons = [[InlineKeyboardButton("👍", callback_data="like")], [InlineKeyboardButton("👎", callback_data="dislike")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons), text="Did you like the image?")

dispatcher.add_handler(CommandHandler('start', startCommand))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('content', content))
dispatcher.add_handler(MessageHandler(Filters.text, messageHandler))

updater.start_polling()
updater.idle()