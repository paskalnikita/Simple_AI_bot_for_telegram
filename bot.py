from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json
updater = Updater(token='Your token') # API token for Telegram
dispatcher = updater.dispatcher

def startCommand(bot, update):
	bot.send_message(chat_id=update.message.chat_id, text='sup?')
def textMessage(bot, update):
	request = apiai.ApiAI('Your Token').text_request() # API tonek for Dialogflow
	request.lang = 'en' # Language of request
	request.session_id = 'BatlabAIBot' # ID of session and dialog
	request.query = update.message.text
	responseJson = json.loads(request.getresponse().read().decode('utf-8'))
	response = responseJson['result']['fulfillment']['speech'] # JSON with answear
	if response:
		bot.send_message(chat_id=update.message.chat_id, text=response)
	else:
		bot.send_message(chat_id=update.message.chat_id, text='Do not understand!')
# Hendlers
start_command_handler = CommandHandler('start', startCommand)
text_message_handler = MessageHandler(Filters.text, textMessage)

dispatcher.add_handler(start_command_handler)
dispatcher.add_handler(text_message_handler)

updater.start_polling(clean=True)
# Ctrl + C stops bot
updater.idle()