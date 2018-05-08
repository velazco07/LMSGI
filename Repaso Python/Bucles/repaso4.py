numero = " "
lista = []
suma = 0
numero = int(input("Introduce un número: "))
while numero != 0:
	lista.append(numero)
	numero = int(input("Introduce un número: "))
for x in lista:
	suma = suma + x
	media = suma/len(lista)	
print("La suma es: ", suma)
print("La media es: ", media)