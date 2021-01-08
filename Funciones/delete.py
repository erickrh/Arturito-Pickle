def delete():
	import pickle
	'''Elimina el elemento que el usuario desee.'''
	print('\n¿WHICH REMINDER DO YOU WANT TO DELETE?\n')
	choose = int(input('> '))
	
	if choose == choose:
		new_list = []

		leer = open('MyApp.pckl', 'rb')
		leer_x2 = pickle.load(leer)
		new_list.extend(leer_x2)
		leer.close()

		eliminar = open('MyApp.pckl', 'wb')
		new_list.pop(choose)
		pickle.dump(new_list, eliminar)
		eliminar.close()

	else:
		print('Por favor elige un recordatorio.')