from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
provincias = doc.findall("provincia/nombre")
for nombre in provincias:
	print(nombre.text)