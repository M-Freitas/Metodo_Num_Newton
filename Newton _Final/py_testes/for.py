# import math
# #
# lista1 = 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
# lista2 = 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
# lista3 = 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9
# length = len(lista1)
# #
# print("--------------------------------------------------------------------------")
# print("Iter\t|D\t\t|F(D)\t\t|F'(D)\t\t||D_(K)-D_(K-1)||\t")
# for i in range(length):		
# 	if i == 0:
# 		print("%s\t|%s\t\t|%s\t\t|%s\t\t|-\t\t|" %(i, lista1[i], lista2[i], lista3[i]))
# 	else:
# 		if i != 18:
# 			iterD = math.fabs(lista1[i] - lista1[i - 1])
# 			print("%s\t|%s\t\t|%s\t\t|%s\t\t|%s\t\t|" %(i, lista1[i], lista2[i], lista3[i], iterD))
# 		else:
# 			iterD = math.fabs(lista1[i + 1] - lista1[i])
# 			print("%s\t|%s\t\t|%s\t\t|%s\t\t|%s\t\t|" %(i, lista1[i], lista2[i], lista3[i], iterD))
# from prettytable import PrettyTable

# x = PrettyTable()
# x.field_names = ["X", "F(X)", "F'(X)"]
# lista1 = 1.123123213, 1.1232143253421314, 1.1341321321412412, 1.123123213, 1.1232143253421314, 1.1341321321412412
# lista2 = 1.123123213, 1.1232143253421314, 1.1341321321412412, 1.123123213, 1.1232143253421314, 1.1341321321412412
# lista3 = 1.123123213, 1.1232143253421314, 1.1341321321412412, 1.123123213, 1.1232143253421314, 1.1341321321412412

# length = len(lista1)
# for i in range(length):
# 	x.add_row([lista1[i], lista2[i], lista3[i]])
# print(x)

z = 0
while (z != 1 and z != 2):
	z = int(input("z: "))
	print(z)