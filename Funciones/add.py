def add():
	import pickle
	'''Este modulo crea un fichero llamado MyApp, en el que se agrega un recordatorio.'''

	lista_recordatorios = []

	try:
		leer = open('MyApp.pckl', 'rb')
		leer_x2 = pickle.load(leer)
		lista_recordatorios.extend(leer_x2)
		leer.close()

	except:
		apoyo = ['apoyo']
		recordario = open('MyApp.pckl', 'wb')
		pickle.dump(apoyo, recordario)
		apoyo.remove('apoyo')
		pickle.dump(apoyo, recordario)
		recordario.close()
		
	print('\nPlease write the reminder\'s name')
	name = input('> ')
	lista_recordatorios.append(name)
		
	recordario = open('MyApp.pckl', 'wb')
	pickle.dump(lista_recordatorios, recordario)
	recordario.close()