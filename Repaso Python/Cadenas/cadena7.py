cadena = input("Introduzca su cadena: ")
lista = cadena.split(" ")
lista2 = []
lista3 = []
for elemento in lista:
	lista2.append(elemento[0])
cadena2 = " ".join(lista2)
for x in lista:
	if x[0]=="a" or x[0]=="A":
		lista3.append(x)
cadena3 = " ".join(lista3)
print(cadena2)
print(cadena.title())
print(cadena3)