def calcular_total_articulos(pba, neuquen, jujuy):

    #Pba
    cantidad_pba = 0

    #Neuquen
    cantidad_neuquen = 0

    #Jujuy
    cantidad_jujuy = 0

    for _ in range(len(pba[1])):
        cantidad_pba += 1

    for _ in range(len(neuquen[1])):
        cantidad_neuquen += 1
    
    for _ in range(len(jujuy[1])):
        cantidad_jujuy += 1

    print(f"Cantidad total de articulos almacenados en el deposito de PBA son: {cantidad_pba}")
    print(f"Cantidad total de articulos almacenados en el deposito de NEUQUEN son: {cantidad_neuquen} ")
    print(f"Cantidad total de articulos almacenados en el deposito de JUJUY son: {cantidad_jujuy}")

def articulos_faltantes(pba,neuquen,jujuy,lista_articulos):

    articulos_faltantes_pba = ""

    for i in range(len(pba[1])):
        for j in range(len(lista_articulos)):
            if pba[i] != lista_articulos[j]:
                articulos_faltantes_pba += lista_articulos[j]
    
    return articulos_faltantes_pba