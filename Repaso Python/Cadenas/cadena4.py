cadena = input("Introduzca una cadena: ")
caracter= input("Introduzca un caracter: ")
for i in cadena:
	cadena=cadena.replace(str(i),caracter)
print (cadena)