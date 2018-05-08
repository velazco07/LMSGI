numerito1 = int(input("Introduce la base de la potencia: "))
numerito2 = int(input("Introduce el exponente de la potencia: "))
multiplicar = 1
contador = 0
while contador != numerito2:
	multiplicar = multiplicar*numerito1
	contador = contador + 1
print(multiplicar)