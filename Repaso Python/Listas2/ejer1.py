num1 = int(input("Introduzca el primer número: "))
num2 = int(input("Introduzca el segundo número: "))
num3 = int(input("Introduzca el tercer número: "))
lista1 = []
lista2 = []
if num1 == num2 or num2 == num3:
	print("No puedes escribir dos números iguales seguidos.")
else:
	if num1 < num2:
		for x in range(num1, num2+1):
			lista1.append(x)
		print(lista1)
	elif num1 > num2:
		for x in range(num1, num2-1, -1):
			lista1.append(x)
		print(lista1)
	if num2 < num3:
		for x in range(num2, num3+1):
			lista2.append(x)
		print(lista2)
	elif num2 > num3:
		for x in range(num2, num3-1, -1):
			lista2.append(x)
		print(lista2)
	lista2.pop(0)
	lista3 = lista1 + lista2
	print(lista3)