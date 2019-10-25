"""
	Ejemplo 1
	autor: jecueva1997
"""
# importacion de librerias
import codecs 
import json
# lectura del archivo txt
archivo = codecs.open("datos.txt", "r")
lineas = archivo.readlines()

# lectura de cuantas lineas existen
# print (len(lineas))

# llamando la libreria de json
linea_diccionario = [json.loads(l) for l in lineas]

# encontrando la posicion de los goles mayores a 3
funcion1 = lambda x: list(x.items())[1][1] >= 3
print("\nLos jugadores que han hecho mas de 3 goles:")
# imprecion de los resultados
print(list(filter(funcion1, linea_diccionario)))


# encontrando los que son de Nigeria
funcion2 = lambda x: list(x.items())[0][1] == "Nigeria"
print("\nLos jugadores que son del país Nigeria:")
# imprecion de los resultados
print(list(filter(funcion2, linea_diccionario)))

# presentacion del valor minimo y maximo de altura
funcion3 = lambda x: list(x.items())[2][1] 
print("\nLa máxima altura de los jugadores es:")
# imprecion de los resultados
print(max(list(map(funcion3, linea_diccionario))))

print("\nLa mínima altura de los jugadores es:")
# imprecion de los resultados
print(min(list(map(funcion3, linea_diccionario))))

