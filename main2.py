from funciones2 import *

tipos_articulos = ["quimico", "trapo", "escoba", "cepillo", "papel higienico", "jabon", "pañuelo descartable"]
precios_articulos = [100,20,40,5,10,4,2]

#1
lista = cargar_secuencialmente()
print(lista)

#2
calcular_tipos_almacenados(lista)

#3
res = calcular_articulos_disponibles(lista, tipos_articulos)

print(res)

#4
calcular_maximos_articulos_almacenados(lista)

#6
calcular_depositos_3_millones(lista)

#7
porcentaje_articulos_x_tipo_totales(lista)


#9
calcular_deposito_mayor_recaudacion(lista, tipos_articulos, precios_articulos)

