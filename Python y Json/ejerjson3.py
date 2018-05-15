# Dime el nombre y el id del/los equipo/s que estan ubicados en Philadelphia
import json
from pprint import pprint
with open("nba.json") as data_file:
	data = json.load(data_file)
for equipo in data:
	if equipo["location"] == "Philadelphia":
		print("Nombre:", equipo["teamName"])
		print("Id:", equipo["teamId"])