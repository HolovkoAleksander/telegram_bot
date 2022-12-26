import telegram.ext
Token = "5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY"
updater = telegram.ext.updater("5408345091:AAFfpuuBU1ragRec9LWU-u8wp_SuZ_RbEQY", use_context = True)
dispatcher = updater.dispatcher

def start(update, context):
    update.message.reply_text("Hello")

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

def content(update, context):
    update.message.reply_text("Wlcome")

def Python(update, context):
    update.message.reply_text("Wlcome : https://www.youtube.com/watch?v=sO42syEV4sY&ab_channel=MarkSolonin")


dispatcher.add_handler(telegram.ext.CommandHandler('start', start))
dispatcher.add_handler(telegram.ext.CommandHandler('help', help))
dispatcher.add_handler(telegram.ext.CommandHandler('content', content))
dispatcher.add_handler(telegram.ext.CommandHandler('Python', Python))

updater.start_polling()
updater.idle()