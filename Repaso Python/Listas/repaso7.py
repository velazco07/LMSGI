lista = []
palabra = input("Introduce las palabra: ")
while palabra != "/":
	lista.append(palabra)
	palabra = input("Introduce las palabra: ")
eliminar = input("Diga la palabra que quiere eliminar: ")
for eliminar in lista:
	lista.remove(eliminar)
print(lista)