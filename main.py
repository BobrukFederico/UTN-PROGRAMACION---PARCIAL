from funciones import calcular_total_articulos, articulos_faltantes

lista_articulos = ["Quimicos", "Trapos", "Escobas", "Cepillos", "Papel higienico", "Jabon", "Pañuelos descartables"]

existencias_pba = [["PBA"],["Quimicos", "Trapos", "Escobas", "Cepillos", "papel higienico"],[10, 20, 50, 70, 90]]

existencias_neuquen = [["Neuquen"],["Escobas", "papel higienico", "jabon"], [20, 4, 31, 200, 10]]

existencias_jujuy = [["Jujuy"],["Quimicos", "Trapos", "Escobas", "Cepillos", "papel higienico", "jabon", "pañuelos descartables"], [20, 30, 44, 75, 31, 220, 10]]


calcular_total_articulos(existencias_pba, existencias_neuquen, existencias_jujuy)


artic_falt = articulos_faltantes(existencias_pba, existencias_neuquen, existencias_jujuy, lista_articulos)
print(artic_falt)