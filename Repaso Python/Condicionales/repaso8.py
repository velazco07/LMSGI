lado1=int(input("Introduce el dato: "))
lado2=int(input("Introduce el dato: "))
lado3=int(input("Introduce el dato: "))
if lado1 == lado2 and lado2 == lado1:
	print("El triangulo es equilatero")
elif lado1==lado2 or lado2==lado3 or lado3==lado1:
	print("El triangulo es Isósceles")
elif lado1^2 == (lado2^2+lado3^2) or lado2^2 == (lado1^2+lado3^2) or lado3^2 == (lado2^2+lado1^2):
	print("Es un triangulo rectangulo")
else:
	print("El triangulo es escaleno")