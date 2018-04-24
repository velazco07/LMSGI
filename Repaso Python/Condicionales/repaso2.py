palabra=int(input("Introduzca su nota: "))
if palabra <= 2:
	print("MD")
elif palabra < 5 and palabra >= 3:
	print("I")
elif palabra == 5:
	print("Suf")
elif palabra == 6:
	print("B")
elif palabra < 9 and palabra >= 7:
	print("Not")
elif palabra <= 10:
	print("Sob")
else:
	print("Error")