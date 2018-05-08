palis = int(input("Introduzca los números para la lista (0 para finalizar): "))
lista = []
listame = []
listama = []
listaig = []
listamu = []
while palis != 0:
	lista.append(palis)
	palis = int(input("Introduzca los números para la lista (0 para finalizar): "))
k = int(input("Introduce un número entero: "))
for x in lista:
	if x > k:
		listama.append(x)
	elif x < k:
		listame.append(x)
	elif x == k:
		listaig.append(x)
	if k%x==0:
		listamu.append(x)
print("Los números mayores son: ", listama)
print("Los números menores son: ", listame)
print("Los números iguales son: ", listaig)
print("Los números multipos son: ", listamu)