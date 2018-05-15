#Haz un programa que pida una ciudad y diga todos lo datos del/los equipo/s de esa ciudad
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
ciudad = input("Introduce la ciudad natal del equipo (La primera letra en mayuscula): ")
for equipo in data:
	if ciudad == equipo["location"]:
		print("Id:", equipo["teamId"])
		print("Abreviación:", equipo["abbreviation"])
		print("Nombre: ", equipo["teamName"])
		print("Nombre comun:", equipo["simpleName"])
		print("Localizacion:", equipo["location"])