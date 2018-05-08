palabra = input("Introduzca una palabra (/ para finalizar): ")
lista = []
listare = []
while palabra != "/":
	lista.append(palabra)
	palabra = input("Introduzca una palabra (/ para finalizar): ")
buscar = input("Introduce la palabra a buscar: ")
print(lista.count(buscar))