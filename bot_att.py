import requests
import time
import json
import os

class TelegramBot:
	def __init__(self):
		token=("5841514465:AAGUaoWGZ3WxCyIkarqmKFE2fmKz25jq5Dc")
		self.iURL=f'https://api.telegram.org/bot{token}/'

	def iniciar(self):
		id_update = None
		whileTrue:
			updated = self.read_new_messages(iUPDATE_ID)
			data = updated["result"]
			if data:
				for dado in data:
					id_update = dado['update_id']
					message = str(dado["message"]["text"])
					chat_id = dado["message"]["from"]["id"]
					first_message = int(dado["message"]["message_id"])==1
					response = self.create_reply(message, first_message)
					self.reply(response, chat_id)

	def read_new_messages(self, id_update):
		link_requested= (f"{self.iURL}getUpdates?timeout=5")
		if id_update:
			link_requested = (f"{link_requested}&offset={id_update+1}")
		iRESULT = requests.get(link_requested)
		return json.loads(iRESULT.content)

	def create_reply(self, message, first_message):
		if first_message == True:
			return (f"Hi,{os.linesep}I'mRobertYourFriend!")

		else:
			return (f"Hi,{os.linesep}I'mRobertYourFriend!{os.linesep}TestDone!")

	def reply(self, response, chat_id):
		link_requested=(f"{self.iURL}sendMessage?chat_id={chat_id}&text={response}")
		requests.get(link_requested)


bot=TelegramBot()
bot.iniciar()