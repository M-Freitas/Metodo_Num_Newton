#coding: utf-8
import math
########
lista_xk = []
lista_resFx = []
lista_resDerFx = []
#FUNÇÃO PARA ESCREVER OS RESULTADOS EM ARQUIVO DE TEXTO
def writeArq(lista1, lista2, lista3):
	arq = open('res_Newton.txt', 'w')
	j = 0
	for i in lista1:
		arq.write('Valor do X_%d: %s\n' %(j, i))
		j = j + 1
	j = 0
	for i in lista2:
		arq.write('Valor do F(X_%d): %s\n' %(j, i))
		j = j + 1
	j = 0
	for i in lista3:
		arq.write('Valor do F_Linha(X_%d): %s\n' %(j, i))
		j = j + 1
	arq.close()
########
#FUNÇÃO PARA CALCULAR O VALOR DE F(D)
def Func(a_3, a_2, d):
	return (a_3*(d**3) - 9*a_2*d + 3)
########
#FUNÇÃO PARA CALCULAR O VALOR DE F'(D)
def Der_Func(a_3, a_2, d):
	return (3*a_3*(d**2) - 9*a_2)
########
#FUNÇÃO PARA TESTE DO CRITERIO DE PARADA |X_K1 - X_K0| <= EPS
def CritParada_Inter(x_k1, x_k, eps):
	# print("|%s - %s| = %s\n" %(x_k1, x_k, math.fabs(x_k1 - x_k)))
	return math.fabs(x_k1 - x_k) <= eps
########
#FUNÇÃO PARA TESTE DO CRITERIO DE PARADA |F(X_K1)| < EPS
def CritParada_Func(a3, a2, x_k, eps):
	return math.fabs(Func(a3, a2, x_k) <= eps)
########
#FUNÇÃO PARA ENCONTRAR A RAIZ APROXIMADA DA FUNÇÃO BASEADO NO METODO DE NEWTON MODIFICADO
def NewtonFL(a3, a2, d0, eps, lmbd, iterMax):	
	#LISTA PARA REGITRAR OS VALORES EM CADA ITERAÇÃO
	lista_xk = []
	lista_resFx = []
	lista_resDerFx = []
	#VARIAVEIS
	k = 0
	x_k1 = 0
	x_k = d0
	x_w = 0
	FL = 0
	#FUNÇÃO CRITERIO DE PARADA PARA A APROXIMAÇÃO INICIAL
	if CritParada_Func(a3, a2, d0, eps):
		lista_resFx.append(Func(a3, a2, x_k))
		lista_resDerFx.append(a3, a2, x_k)
		lista_xk.append(x_k)
		#RETORNO DAS LISTAS
		return  lista_xk, lista_resFx, lista_resDerFx
	#LOOP DE ITERAÇÃO PARA ENCONTRAR A RAIZ APROXIMADA
	while k <= iterMax:
		FL = Der_Func(a3, a2, x_k)
		#CONDIÇÃO |F'(X_0)| >=  λ
		if math.fabs(FL >= lmbd):
			#REGISTRANDO OS VALORES DO D_0 NA LISTA DE RESULTADO
			if k == 0:
				lista_resFx.append(Func(a3, a2, x_k))
				lista_resDerFx.append(FL)
				lista_xk.append(x_k)
			#INICIO DE METODO
			x_w = x_k
			#CONDIÇÃO CASO |F'(X_k)| < λ
			if math.fabs(Der_Func(a3, a2, x_k) < lmbd):
				FL = Der_Func(a3, a2, x_w)
			#CONDIÇÃO CASO |F'(X_k)| > λ
			else:
				x_k1 = x_k - (Func(a3, a2, x_k)/FL)
				lista_resFx.append(Func(a3, a2, x_k1)) #REGISTRANDO O VALOR DE F(X_K1)
				lista_resDerFx.append(FL)			   #REGISTRANDO O VALOR DE F'(X_K1)
				lista_xk.append(x_k1)				   #REGISTRANDO O VALOR DE X_K1
			#######
			#CRITERIO DE PARADA DO METODO |X_K1 - X_K0| <= EPS OU |F(X_K1)| < EPS or CritParada_Func(a3, a2, x_k1, eps)
			if CritParada_Inter(x_k1, x_k, eps):
				#RETORNO DAS LISTAS COM OS VALORES DE CADA ITERAÇÃO
				return lista_xk, lista_resFx, lista_resDerFx
			#######
			#ATUALIZANDO OS VALORES DE X_K E K
			x_k = x_k1
			k += 1
	########
	#CASO O NÚMERO DE ITERAÇÃO SEJA EXCEDIDO
	return lista_xk, lista_resFx, lista_resDerFx
########
def Registrar_Lista(a3, a2, x_k):
	lista_resFx.append(Func(a3, a2, x_k))
	lista_resDerFx.append(Der_Func(a3, a2, x_k))
	lista_xk.append(x_k)
########
#FUNÇÃO PARA ENCONTRAR A RAIZ APROXIMADA DA FUNÇÃO BASEADO NO METODO DE NEWTON MODIFICADO
def OG_Newton(a3, a2, d0, eps, lmbd, iterMax):
	#LISTA PARA REGITRAR OS VALORES EM CADA ITERAÇÃO
	# lista_xk = []
	# lista_resFx = []
	# lista_resDerFx = []
	#VARIAVEIS
	k = 0
	x_k1 = 0
	x_k = d0
	flag = True
	#FUNÇÃO CRITERIO DE PARADA PARA A APROXIMAÇÃO INICIAL
	if CritParada_Func(a3, a2, d0, eps):
		Registrar_Lista(a3, a2, x_k)
		# lista_resFx.append(Func(a3, a2, x_k))
		# lista_resDerFx.append(Der_Func(a3, a2, x_k))
		# lista_xk.append(x_k)
		#RETORNO DAS LISTAS
		return  lista_xk, lista_resFx, lista_resDerFx
	#LOOP DE ITERAÇÃO PARA ENCONTRAR A RAIZ APROXIMADA
	while k <= iterMax:
		if k == 0:
			Registrar_Lista(a3, a2, x_k)
			# lista_resFx.append(Func(a3, a2, x_k))
			# lista_resDerFx.append(Der_Func(a3, a2, x_k))
			# lista_xk.append(x_k)
		else:
			x_k1 = x_k - (Func(a3, a2, x_k)/Der_Func(a3, a2, x_k))
			Registrar_Lista(a3, a2, x_k1)
			# lista_resFx.append(Func(a3, a2, x_k1)) 					   #REGISTRANDO O VALOR DE F(X_K1)
			# lista_resDerFx.append(Der_Func(a3, a2, x_k1))			   #REGISTRANDO O VALOR DE F'(X_K1)
			# lista_xk.append(x_k1)				   					   #REGISTRANDO O VALOR DE X_K1
			#######
			#CRITERIO DE PARADA DO METODO |X_K1 - X_K0| <= EPS OU |F(X_K1)| < EPS
			if CritParada_Inter(x_k1, x_k, eps):
				#RETORNO DAS LISTAS COM OS VALORES DE CADA ITERAÇÃO
				flag = False
				return lista_xk, lista_resFx, lista_resDerFx, flag
			#ATUALIZANDO OS VALORES DE X_K
			x_k = x_k1
		#INCREMENTA O VALOR DE K
		k += 1
	#CASO O NÚMERO DE ITERAÇÃO SEJA EXCEDIDO
	return lista_xk, lista_resFx, lista_resDerFx, flag