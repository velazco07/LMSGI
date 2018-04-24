numero = int(input("Introduce un número: "))
factorial = 1
while numero > 0:
	factorial*=numero
	numero-=1
print(factorial)