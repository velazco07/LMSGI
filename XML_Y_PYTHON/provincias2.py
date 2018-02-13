from lxml import etree
doc = etree.parse('provinciasypoblaciones.xml')
municipio = doc.findall("provincia/localidades/localidad")
for nombre in municipio:
	print(nombre.text)