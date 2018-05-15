# Haz un programa que pida por teclado la abreviacion y te de el nombre del equipo y 
# el dato que quieres mirar
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
simple = input("Introduce la abreviación (En mayusculas): ")
modo = input("¿Qué quieres ver? (id, nombre, mote, localizacion): " )
if modo == "id":	
	for equipo in data:
		if simple == equipo["abbreviation"]:
			print("Id:", equipo["teamId"])
elif modo == "nombre":
	for equipo in data:
		if simple == equipo["abbreviation"]:
			print("Nombre:", equipo["teamName"])
elif modo == "mote":
	for equipo in data:
		if simple == equipo["abbreviation"]:
			print("Mote:", equipo["simpleName"])
elif modo == "localizacion":
	for equipo in data:
		if simple == equipo["abbreviation"]:
			print("Nombre:", equipo["location"])
else:
	print("No existe ese modo")



