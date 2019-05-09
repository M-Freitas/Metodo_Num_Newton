#coding: utf-8
import math
from prettytable import prettytable

#LISTA GLOBAIS PARA REGITRAR OS VALORES EM CADA ITERAÇÃO
lista_xk = []
lista_resFx = []
lista_resDerFx = []
#FUNÇÃO PARA CALCULAR O VALOR DE F(D)
def Func(a3, a2, d):
	return (a3*(d**3) - 9*a2*d + 3)
#FUNÇÃO PARA CALCULAR O VALOR DE F'(D)
def Der_Func(a3, a2, d):
	h = 0.0000000001
	return((Func(a3, a2, d + h) - Func(a3, a2, d - h))/(2 * h))
#FUNÇÃO PARA TESTE DO CRITERIO DE PARADA |X_K1 - X_K0| <= EPS
def CritParada_Inter(x_k1, x_k, eps):
	return (math.fabs(x_k1 - x_k) <= eps)
#FUNÇÃO PARA TESTE DO CRITERIO DE PARADA |F(X_K1)| < EPS
def CritParada_Func(a3, a2, x_k, eps):
	return ((math.fabs(Func(a3, a2, x_k))) < eps)
#FUNÇÃO PARA ENTRADA DE SOMENTE VALORES MAIORES QUE ZERO
def dif_zero(var, opc):
	if opc == 'float':
		num = float(input("Digite o valor para %s: " %var))
		return num
	#########
	if opc == 'float*':
		num = float(input("Digite o valor para %s: " %var))
	else:
		num = int(input("Digite o valor para %s: " %var))
	while num <= 0:
		if opc == 'float*':
			num = float(input("Digite o valor, MAIOR QUE ZERO, para %s: " %var))
		else:
			num = int(input("Digite o valor, MAIOR QUE ZERO, para %s: " %var))
	return num
#FUNÇÃO PARA IMPRIMIR OS DADOS EM TXT
def writeArq(lista1, lista2, lista3, opc):
	table = PrettyTable()
	if opc == 1:
		arq = open('res_OG_Newton.txt', 'a')
		
	else:
		arq = open('res_Newton_FL.txt', 'a')
	######
	table.title = "Valores durante a execução do método"
	table.field_names = ["Iteração", "D", "F(D)", "F'(D)", "|D_(K)-D_(K-1)|"]
	######
	length = len(lista1)
	for i in range(length):
		if i == 0:
			table.add_row([i, lista1[i], lista2[i], lista3[i], "-"])
		elif i != length:
			iterD = math.fabs(lista1[i] - lista1[i - 1])
			table.add_row([i, lista1[i], lista2[i], lista3[i], iterD])
		else:
			iterD = math.fabs(lista1[i + 1] - lista1[i])
			table.add_row([i, lista1[i], lista2[i], lista3[i], iterD])
	arq.write(str(table))
	arq.write("\n-------------------------------------------------------------------------------------------------------\n\n\n")
	arq.close() 
#FUNÇÃO PARA REGISTRAR OS VALORES DO MÉTODO EM CADA ITERAÇÃO
def Registrar_Lista(a3, a2, x_k, FL, opc):
	if opc:
		lista_resDerFx.append(FL)	
	else:
		lista_resDerFx.append(Der_Func(a3, a2, x_k))

	lista_resFx.append(Func(a3, a2, x_k))
	lista_xk.append(x_k)
#FUNÇÃO PARA ENCONTRAR A RAIZ APROXIMADA DA FUNÇÃO BASEADO NO METODO DE NEWTON MODIFICADO
def NewtonFL(a3, a2, d0, lmbd, eps, iterMax):
	#VARIAVEIS
	k = 0
	x_k = d0
	x_k1 = 0
	x_w = 0
	FL = 0
	flag = True
	#####
	if CritParada_Func(a3, a2, d0, eps):					#FUNÇÃO CRITERIO DE PARADA PARA A APROXIMAÇÃO INICIAL
		flag = -1
		Registrar_Lista(a3, a2, x_k, FL, False)				#REGISTRARÁ OS VALORES DE F(X_K), F'(X_K) E X_K
		return  lista_xk, lista_resFx, lista_resDerFx, flag	#RETORNO DAS LISTAS
	#####
	FL = Der_Func(a3, a2, x_k)
	if (math.fabs(FL)) >= lmbd:								#CONDIÇÃO |F'(X_0)| >=  λ
		#LOOP DE ITERAÇÃO PARA ENCONTRAR A RAIZ APROXIMADA
		while k <= iterMax:
			FL = Der_Func(a3, a2, x_k)
			#REGISTRANDO OS VALORES DO D_0 NA LISTA DE RESULTADO
			if k == 0:
				Registrar_Lista(a3, a2, x_k, FL, False)		#REGISTRA OS VALORES DE F(X_K), F'(X_K) E X_K
				x_w = x_k
			#INICIO DE METODO
			else:
				if (math.fabs(Der_Func(a3, a2, x_k))) < lmbd:#CONDIÇÃO CASO |F'(X_k)| < λ
					FL = Der_Func(a3, a2, x_w)

				#CONDIÇÃO CASO |F'(X_k)| > λ
				x_k1 = x_k - (Func(a3, a2, x_k)/FL)
				Registrar_Lista(a3, a2, x_k1, FL, True)		#REGISTRANDO OS VALORES DE F(X_K1), FL E X_K1
				if CritParada_Inter(x_k1, x_k, eps):		#CRITERIO DE PARADA DO METODO |X_K1 - X_K0| <= EPS
					flag = False
					#RETORNO DAS LISTAS COM OS VALORES DE CADA ITERAÇÃO
					return lista_xk, lista_resFx, lista_resDerFx, flag	
				#ATUALIZANDO O VALOR DE X_K
				x_w = x_k
				x_k = x_k1
			#INCREMENTA O VALOR DE K
			k += 1
	else:
		#CASO O NÃO ATENDA A SUPOSIÇÃO INICIAL DO MÉTODO
		flag = -2

	#CASO O NÚMERO DE ITERAÇÃO SEJA EXCEDIDO
	return lista_xk, lista_resFx, lista_resDerFx, flag
#FUNÇÃO PARA ENCONTRAR A RAIZ APROXIMADA DA FUNÇÃO BASEADO NO METODO DE NEWTON MODIFICADO
def OG_Newton(a3, a2, d0, lmbd, eps, iterMax):
	#VARIAVEIS
	k = 0
	x_k = d0
	x_k1 = 0
	flag = True
	######
	if CritParada_Func(a3, a2, d0, eps):					#FUNÇÃO CRITERIO DE PARADA PARA A APROXIMAÇÃO INICIAL
		flag = -1
		Registrar_Lista(a3, a2, x_k, 0, False)				#REGISTRARÁ OS VALORES DE F(X_K), F'(X_K) E X_K
		return  lista_xk, lista_resFx, lista_resDerFx, flag	#RETORNO DAS LISTAS
	#LOOP DE ITERAÇÃO PARA ENCONTRAR A RAIZ APROXIMADA
	while k <= iterMax:
		if k == 0:
			Registrar_Lista(a3, a2, x_k, 0, False)		#REGISTRANDO OS VALORES DE F(X_K), F'(X_K) E X_K
		else:
			x_k1 = x_k - (Func(a3, a2, x_k)/Der_Func(a3, a2, x_k))
			Registrar_Lista(a3, a2, x_k1, 0, False)		#REGISTRANDO OS VALORES DE F(X_K1), F'(X_K1) E X_K1
			if CritParada_Inter(x_k1, x_k, eps):		#CRITERIO DE PARADA DO METODO |X_K1 - X_K0| <= EPS OU |F(X_K1)| < EPS
				flag = False							
				#RETORNO DAS LISTAS COM OS VALORES DE CADA ITERAÇÃO
				return lista_xk, lista_resFx, lista_resDerFx, flag
			#ATUALIZANDO O VALOR DE X_K
			x_k = x_k1
		#INCREMENTA O VALOR DE K
		k += 1
	#CASO O NÚMERO DE ITERAÇÃO SEJA EXCEDIDO
	return lista_xk, lista_resFx, lista_resDerFx, flag
