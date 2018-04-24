numero = int(input("Dame un número entre 0 y 9: "))
if numero > 0 or numero <=9:
	for contador in range(15):
		contador = contador + 1
		multiplicar = contador*numero
		print(multiplicar)