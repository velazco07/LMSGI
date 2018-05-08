num = int(input("Introduce un número: "))
lista = []
lista2 = []
while num >= 0:	
	lista.append(num)
	num=int(input("Introduce un número: "))
for x in lista:
	if x%2==0:
		lista2.append(x)
print(max(lista))
print(lista2)