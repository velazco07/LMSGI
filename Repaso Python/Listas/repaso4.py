palabras = input("Introduce una palabras (/ para finalizar): ")
lista = []
while palabras != "/":
	lista.append(palabras)
	palabras = input("Introduce palabras (/ para finalizar): ")
lista.reverse()
print(lista)