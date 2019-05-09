# #coding: utf-8
import funcs, menu
from prettytable import prettytable
######
menu.menu()
print("-------- Atribuição de Valores --------\n")
a_3 = funcs.dif_zero('A_(3)', 'float')
a_2 = funcs.dif_zero('A_(2)', 'float')
d_0 = funcs.dif_zero('D_(0) - [Aproximação Inicial]', 'float')
lmb = funcs.dif_zero('Lambda', 'float*')
eps = funcs.dif_zero('Épsilon', 'float*')
iterMax = funcs.dif_zero('iterações máximas', 'int*')
menu.clear()
######
table_values = prettytable.PrettyTable()
table_values.title = "---- Tabela de Valores ----"
table_values.field_names = ["Valores das Variáveis"]
table_values.align["Valores das Variáveis"] = 'l'
######
table_values.add_row(["Valor de A_(3): %s" %a_3])
table_values.add_row(["Valor de A_(2): %s" %a_2] )
table_values.add_row(["Valor de D_(0): %s" %d_0])
table_values.add_row(["Valor de Lambda: %s" %lmb])
table_values.add_row(["Valor de Épsilon: %s" %eps])
table_values.add_row(["Iterações Máximas: %s" %iterMax])
######
print(table_values)
opc_met = int(input("Escolha um das opções para selecionar o método a ser utilizado\n[1 - MÉTODO DE NEWTON || 2 - MÉTODO DE NEWTON(FL)]\n\nOpcão: "))
while (opc_met != 1 and opc_met != 2):
	opc_met = int(input("Escolha um das opções listas\n[1 - Método de Newton || 2 - Método de Newton(FL)]\nOpção: "))
print("\n")
menu.enter('met')
menu.clear()
if opc_met == 1:
	arq = open('res_OG_Newton.txt', 'a')
	arq.write("\n\n------------ MÉTODO DE NEWTON -----------\n\n")
	(raizAnt_NewtonNormal , vlr_Fx, vlr_DerFx, erro) = funcs.OG_Newton(a_3, a_2, d_0, lmb, eps, iterMax)
else:
	arq = open('res_Newton_FL.txt', 'a')
	arq.write("\n\n------------ MÉTODO DE NEWTON[FL] -----------\n\n")
	(raizAnt_NewtonNormal , vlr_Fx, vlr_DerFx, erro) = funcs.NewtonFL(a_3, a_2, d_0, lmb, eps, iterMax)
####
arq.write(str(table_values))
arq.write("\n\n")
arq.close()
######
if erro == -1:
	print("\nMétodo executado com sucesso!Sua aproximação inicial já era a raiz!!!")
if erro == False:
	print("\nMétodo executado com sucesso!!!")
if erro == True:
	print("\nMétodo excedeu o número de iterações estipuladas!!!")
if erro == -2:
	print("\nValor da aproximação inicial não respeita a suposição |F'(D_(0)| >= Lambda")
########
if opc_met == 1:
	print("Resultados do método foram arquivados em res_OG_Newton.txt\n")
else:
	print("Resultados do método foram arquivados em res_Newton_FL.txt\n")

funcs.writeArq(raizAnt_NewtonNormal , vlr_Fx, vlr_DerFx, opc_met)
