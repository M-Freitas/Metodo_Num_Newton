#coding: utf-8
import os, platform
from prettytable import PrettyTable
#
def clear():
	if(platform.system()) == 'Windows':
		os.system('cls')
	else:
		os.system('clear')
def enter(opc):
	if opc == 'met':
		input("Pressione a tecla ENTER para o método ser executado")
	else:
		input("Pressione a tecla ENTER para continuar")
def menu():
	table = PrettyTable()
	table.title = "--------- Método de Newton/Newton - FL --------- "
	table.field_names = ["Serão necessários a entrada dos seguinte dados"]
	table.align["Serão necessários a entrada dos seguinte dados"] = 'l'
	#
	table.add_row(["1ª Valor de A_(3)"])
	table.add_row(["1ª Valor de A_(2)"])
	table.add_row(["3º Valor da D_(0) - (Aproximação inicial)"])
	table.add_row(["4ª Valor de Lambda"])
	table.add_row(["5ª Valor de Épsilon"])
	table.add_row(["6ª Valor do número de iterações máximas"])
	table.add_row(["7ª Opção do método a ser utilizado"])
	print(table)
	#######
	print('\n')
	enter('')
	clear()
