lista = []
for x in range(10):
	numerito=int(input("Introduce un número: "))
	lista.append(numerito)
for numero in lista:
	if numero > 0:
		print("El número es positivo")
	elif numero < 0:
		print("El número es negativo")
	else:
		print("Eĺ número es 0")