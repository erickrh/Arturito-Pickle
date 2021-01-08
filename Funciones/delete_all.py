def delete_all():
	'''Elimina todos los recordatorios del fichero MyApp.'''
	try:
		print('¿Desea eliminar todos los recordatorios?\ny/n')
		respuesta = input('> ')
		
		if respuesta == 'y':
			import pickle
			lista_vacia = []
			borrar_todo = open('MyApp.pckl', 'wb')
			pickle.dump(lista_vacia, borrar_todo)
			borrar_todo.close()
			print('\nLista actualizada:')
		elif respuesta == 'n':
			pass
		else:
			print('Please try again.')
			
	except Exception as error_delete_all:
		print('Se ha presentado un error: {}'.format(error_delete_all))