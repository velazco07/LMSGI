cadena=input("Escribe un Numero binario: ")		
contador=0
numero=0
for i in cadena[::-1]:
	if i=="1":
		numero=numero+(2**contador)
	contador=contador+1
print(numero)