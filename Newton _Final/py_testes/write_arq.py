def writeArq(lista1, lista2, lista3, opc):
	if opc == 1:
		arq = open('res_OG_Newton.txt', 'w')
		
	else:
		arq = open('res_Newton_FL.txt', 'w')
	####	
	arq.write("---------------------------------------------------------------------\n")
	arq.write("Iter\t|D 						\t\t|F(D)					\t\t|F'(D)					\t\t||D_(K)-D_(K-1)|\t|\n")
	length = len(lista1)
	##
	for i in range(length):		
		if i == 0:
			arq.write("%s 		\t|%0.8f	\t\t|%0.8f	\t\t|%0.8f			\t\t|-						\t\t|\n" %(i, lista1[i], lista2[i], lista3[i]))
		else:
			if i != length:
				iterD = math.fabs(lista1[i] - lista1[i - 1])
				arq.write("%s 		\t|%0.8f	\t\t|%.8f	 \t\t|%0.8f 	   \t\t|%0.8f		\t\t|\n" %(i, lista1[i], lista2[i], lista3[i], iterD))
			else:
				iterD = math.fabs(lista1[i + 1] - lista1[i])
				arq.write("%s 		\t|%0.8f	\t\t|%.8f	 \t\t|%0.8f		   \t\t|%0.8f		\t\t|\n" %(i, lista1[i], lista2[i], lista3[i], iterD))
	arq.write("---------------------------------------------------------------------")

# (raizAnt_NewtonNormal , vlr_Fx, vlr_DerFx, erro) = funcs.OG_Newton(a_3, a_2, d_0, lmb, epsln, iterMxm)
# funcs.writeArq(raizAnt_NewtonNormal2 , vlr_Fx2, vlr_DerFx2, 2)