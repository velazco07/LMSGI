palabra = input("Introduzca una letra: ")
while palabra != ' ':
	if palabra == 'a' or palabra == 'e' or palabra == 'i' or palabra == 'o' or palabra == 'u':
		print("VOCAL")
		palabra = input("Introduzca una letra: ")	
	elif palabra == "0" or palabra == "1" or palabra == "2" or palabra == "3" or palabra == "4" or palabra == "5" or palabra == "6" or palabra == "7" or palabra == "8" or palabra == "9":
	 	print("NUMERO")
	 	palabra = input("Introduzca una letra: ")
	else:
		print("CONSONANTE")
		palabra = input("Introduzca una letra: ")
print("CRUK")