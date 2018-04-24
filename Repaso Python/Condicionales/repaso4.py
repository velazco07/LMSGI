dia=int(input("Introduce un número(Entre 1 y 12)"))
if dia == 1 and dia == 3 and dia == 5 and dia == 7 and dia == 8 and dia == 10 and dia == 12:
	print("Tiene 31 días")
elif dia == 4 and dia == 6 and dia == 9 and dia == 11:
	print("Tiene 30 días")
elif dia == 2:
	print("Puede tener 28 o 29 días")
else:
	print("DEL 1 AL 12!!!!!")