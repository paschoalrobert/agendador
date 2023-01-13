#Libs
from openyxl import Workbook, load_workbook
from datetime import datetime


class Excel_Model:
	def __init__(self):
		wb = load_workbook("/data/milho_verde.xlsx/") 	#Abre Planilha .xlsx
		self.sheet = []
		for sheet in wb: 				#Procura Abas salvas
			self.sheet.append(sheet)		#Adiciona Abas Ativas no Array
			
	def banner(self):
		pass
	
	def time(self):
		self.time = datetime.now()
		self.dia_semana = datetime.today().weekday()
		if 0 == self.dia_semana:
			print("Segunda-Feira")
		elif 1 == self.dia_semana:
			print("Terça-Feira")
		elif 2 == self.dia_semana:
			print("Quarta-Feira")

		elif 3 == self.dia_semana:
			print("Quinta-Feira")
		elif 4 == self.dia_semana:
			print("Sexta-Feira")
		elif 5 == self.dia_semana:
			print("Sabado")
		elif 6 == self.dia_semana:
			print("Domingo")
		else:
			pass

		