def show_reminders():
	'''Nos muestras todos los recordatorios añadidos en el fichero MyApp.'''
	import pickle

	try:
		print('\nLISTA:\n')
		recordario = open('MyApp.pckl', 'rb')
		leer = pickle.load(recordario)
		
		for i, ii in enumerate(leer):
			print('{a} - {b}'.format(a = i, b = ii))

		recordario.close()

	except:
		print('No hay ningún recordario.')