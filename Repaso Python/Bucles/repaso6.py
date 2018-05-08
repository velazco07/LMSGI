num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce el siguiente número: "))
for x in range(num1, num2 + 1):
	if x%2==0:
		print(x)