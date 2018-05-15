# Dime el nombre comun y la localización de los equipos cuya abreviación sea NYK
import json
from pprint import pprint
with open("nba.json") as data_file:
	data=json.load(data_file)
for equipo in data:
	if equipo["abbreviation"] == "NYK":
		print(equipo["simpleName"])
		print(equipo["abbreviation"])