numero = int(input("Introduce un número: "))
numeroa = " "
while numeroa != numero:
	numeroa = int(input("Acierta el número: "))
	if numeroa > numero:
		print("Este número es mayor que el primero: ")
	elif numeroa < numero:
		print("Este número es menor que el primero: ")
	else:
		break
print("Has acertado")