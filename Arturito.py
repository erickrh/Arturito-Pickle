#!/usr/bin/python3
from io import open
import pickle
from Funciones import (add,
						show_reminders,
						delete,
						delete_all)

# Se crea con el fin de mantener el programa abierto después de realizar alguna operación dentro de él.
interruptor = True
while interruptor:

	print('''
	Welcome to Arturito. Please write an option:
	1) Add a reminder
	2) Delete a reminder
	3) Show reminders
	4) Refresh / Delete all reminders
	5) Exit
	''')

	try:
		def main():

			# Pregunta al usuario acerca de cual es la opción que desea, tomando como nombre 'option'.
			option = int(input('> '))
			if option == 1:
				add()
				show_reminders()

			elif option == 2:
				show_reminders()
				delete()
				print('\nList update.')
				show_reminders()

			elif option == 3:
				print('\nTHESE ARE ALL OF YOUR REMINDERS:')
				show_reminders()

			elif option == 4:
				delete_all()
				show_reminders()

			elif option == 5:
				global interruptor
				interruptor = False

			else:
				print('Please try again.')	

		main()

	# Nos permite visualizar si existe algún error.
	except Exception as error0:
		print('Hemos encontrado un error: {}'.format(error0))

	finally:
		print('\n')