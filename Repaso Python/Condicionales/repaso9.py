año = int(input("Introduce el año: "))
if año % 4 == 0 or año %	 400 == 0:
	print("Es un año bisiesto")
elif año % 100 == 0:
	print("No es un año bisiesto")