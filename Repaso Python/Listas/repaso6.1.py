lista = []
palabra = input("Introduce las palabras de la lista (/ para finalizar): ")
while palabra != "/":
	lista.append(palabra)
	palabra = input("Introduce las palabras de la lista (/ para finalizar): ")
buscar = input("Introduce la palabra que quieres buscar: ")
sustituir = input("Introduce la palabra por la que la quieres sustituir: ")
while buscar in lista:
	lista[lista.index(buscar)]=sustituir
print(lista)