from datetime import datetime

dia_semana = datetime.today().weekday()
print(dia_semana)

if 0 == dia_semana:
    print("Segunda-Feira")
elif 1 == dia_semana:
    print("Terça-Feira")
elif 2 == dia_semana:
	print("Quarta-Feira")
elif 3 == dia_semana:
	print("Quinta-Feira")
elif 4 == dia_semana:
	print("Sexta-Feira")
elif 5 == dia_semana:
	print("Sabado")
elif 6 == dia_semana:
	print("Domingo")