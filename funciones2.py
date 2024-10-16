def cargar_secuencialmente():
    parar = False
    lista_completa = []

    while not parar:
        lista = [0] * 3
        lista[0] = input("Ingrese la provincia: ")
        lista[1] = input("Ingrese el tipo de articulo: ")
        lista[2] = int(input("Ingrese la cantidad: "))

        lista_completa += [lista]

        seguir = input("Quiere seguir? si/no: ")
        if seguir != "no" and seguir != "si":
            seguir = input("Error. Quiere seguir? si/no: ")
        
        if seguir == "no":
            parar = True

    return lista_completa

def calcular_tipos_almacenados(lista):

    #PBA
    articulos_p = 0
    #Neuquen
    articulos_n = 0
    #Jujuy
    articulos_j = 0

    for i in range(len(lista)):
        tipo = lista[i][1]
        deposito = lista[i][0]

        if deposito == "pba":
            articulos_p += 1
        elif deposito == "neuquen":
            articulos_n += 1
        elif deposito == "jujuy":
            articulos_j += 1
        #for j in range(len(lista[i])):
    print(f"Articulos almacenados en el deposito de pba son: {articulos_p}")
    print(f"Articulos almacenados en el deposito de neuquen son: {articulos_n}")
    print(f"Articulos almacenados en el deposito de jujuy son: {articulos_j}")

def calcular_articulos_disponibles(lista, articulos):

    #PBA
    articulos_iguales_pba = []

    #Neuquen
    articulos_iguales_neuquen = []

    #Jujuy
    articulos_iguales_jujuy = []


    articulos_iguales_pba = []


    articulos_faltantes_pba = []

    for i in range(len(lista)):
        tipo = lista[i][1]
        deposito = lista[i][0]
        for j in range(len(articulos)):
            if deposito == "pba":
                if tipo == articulos[j]:
                    articulos_iguales_pba += [articulos[j]]
                # elif tipo != articulos[j]:
                #     articulos_faltantes_pba += [articulos[j]]
            elif deposito == "neuquen":
                if tipo == articulos[j]:
                    articulos_iguales_neuquen += [articulos[j]]
            elif deposito == "jujuy":
                if tipo == articulos[j]:
                    articulos_iguales_jujuy += [articulos[j]]





    # indice = 0
    # for e in articulos_iguales_pba:
    #     encontrado = False
    #     for h in articulos:
    #         if e == h:
    #             encontrado = True
    #             break
    #     if not encontrado:
    #         articulos_faltantes_pba[indice] = e
    #         indice += 1
    
    # for h in articulos:
    #     encontrado = False
    #     for e in articulos_iguales_pba:
    #         if h == e:
    #             encontrado = True
    #             break
    #     if not encontrado:
    #         articulos_faltantes_pba[indice] = h
    #         indice += 1

    # lista_final_pba = [0] * indice
    # for i in range(indice):
    #     lista_final_pba[i] = articulos_faltantes_pba[i]
            


    
    print(f"Articulos disponibles en el deposito de pba son: {articulos_iguales_pba}")
    print(f"Articulos disponibles en el deposito de neuquen son: {articulos_iguales_neuquen}")
    print(f"Articulos disponibles en el deposito de jujuy son: {articulos_iguales_jujuy}")

    # return lista_final_pba


def calcular_maximos_articulos_almacenados(lista):

    #PBA
    max_articulo_pba = ""
    max_cantidad_pba = 0
    #Neuquen
    max_articulo_n = ""
    max_cantidad_n = 0
    #Jujuy
    max_articulo_j = ""
    max_cantidad_j = 0

    for i in range(len(lista)):
        tipo = lista[i][1]
        deposito = lista[i][0]
        cantidad = lista[i][2]

        if deposito == "pba":
            if cantidad > max_cantidad_pba:
                max_cantidad_pba = cantidad
                max_articulo_pba = tipo
        elif deposito == "neuquen":
            if cantidad > max_cantidad_n:
                max_cantidad_n = cantidad
                max_articulo_n = tipo
        elif deposito == "jujuy":
            if cantidad > max_cantidad_j:
                max_cantidad_j = cantidad
                max_articulo_j = tipo
    print(f"El articulo con mas cantidad del deposito de pba es: {max_articulo_pba}")
    print(f"El articulo con mas cantidad del deposito de neuquen es: {max_articulo_n}")
    print(f"El articulo con mas cantidad del deposito de jujuy es: {max_articulo_j}")


def calcular_depositos_3_millones(lista):

    #PBA
    cantidad_total_pba = 0

    #Neuquen
    cantidad_total_neuquen = 0

    #Jujuy
    cantidad_total_jujuy = 0

    #Total
    cantidad_depositos_3_millones = 0
    provincias = ""

    for i in range(len(lista)):
        deposito = lista[i][0]
        cantidad = lista[i][2]

        match deposito:
            case "pba":
                cantidad_total_pba += cantidad
            case "neuquen":
                cantidad_total_neuquen += cantidad
            case "jujuy":
                cantidad_total_jujuy += cantidad
    
    if cantidad_total_pba >= 3000000:
        cantidad_depositos_3_millones += 1
        provincias += "pba "
    if cantidad_total_neuquen >= 3000000:
        cantidad_depositos_3_millones += 1
        provincias += "neuquen "
    if cantidad_total_jujuy >= 3000000:
        cantidad_depositos_3_millones += 1
        provincias += "jujuy "

    print(f"El total de depositos que pasaron las 3 millones de unidades fueron: {cantidad_depositos_3_millones}, las provincias fueron: {provincias}")


#En la consigna no especifica si es por provincia o articulos totales
def porcentaje_articulos_x_tipo_totales(lista):
    
    total_articulos_almacenados = 0
    trapos = 0
    cepillos = 0
    papel_higienico = 0
    jabon = 0
    pañuelo_descartable = 0
    quimico = 0
    escoba = 0
    
    porcentaje_trapo = 0
    porcentaje_escoba = 0
    porcentaje_quimico = 0
    porcentaje_jabon = 0
    porcentaje_papel_higienico = 0
    porcentaje_pañuelo_dc = 0
    porcentaje_cepillo = 0


    for i in range(len(lista)):
        tipo = lista[i][1]
        
        #match tipo:
        #    case == "trapo"
            #     trapos += 1
            #     total_articulos_almacenados += 1
            #  case == "cepillo":
        if tipo == "trapo":
            trapos += 1
            total_articulos_almacenados += 1
        elif tipo == "cepillo":
            cepillos += 1
            total_articulos_almacenados += 1
        elif tipo == "papel higienico":
            papel_higienico += 1
            total_articulos_almacenados += 1
        elif tipo == "jabon":
            jabon += 1
            total_articulos_almacenados += 1
        elif tipo == "pañuelo descartable":
            pañuelo_descartable += 1
            total_articulos_almacenados += 1
        elif tipo == "quimico":
            quimico += 1
            total_articulos_almacenados += 1
        elif tipo == "escoba":
            escoba += 1
            total_articulos_almacenados += 1

    if trapos != 0:
        porcentaje_trapo = int((trapos / total_articulos_almacenados) * 100)
    if cepillos != 0:
        porcentaje_cepillo = int((cepillos / total_articulos_almacenados) * 100)
    if papel_higienico != 0:
        porcentaje_papel_higienico = int((papel_higienico / total_articulos_almacenados) * 100)
    if jabon != 0:
        porcentaje_jabon = int((jabon / total_articulos_almacenados) * 100)
    if pañuelo_descartable != 0:
        porcentaje_pañuelo_dc = int((pañuelo_descartable / total_articulos_almacenados) * 100)
    if quimico != 0:
        porcentaje_quimico = int((quimico / total_articulos_almacenados) * 100)
    if escoba != 0:
        porcentaje_escoba = int((escoba / total_articulos_almacenados) * 100)


    print(f"Total articulos almacenados {total_articulos_almacenados}")
    print(f"Porcentaje de trapos almacenados: {porcentaje_trapo}%")
    print(f"Porcentaje de cepillos almacenados: {porcentaje_cepillo}%")
    print(f"Porcentaje de papeles higienicos almacenados: {porcentaje_papel_higienico}%")
    print(f"Porcentaje de jabones almacenados: {porcentaje_jabon}%")
    print(f"Porcentaje de pañuelos descartables almacenados: {porcentaje_pañuelo_dc}%")
    print(f"Porcentaje de quimicos almacenados: {porcentaje_quimico}%")
    print(f"Porcentaje de escobas almacenados: {porcentaje_escoba}%")


def calcular_deposito_mayor_recaudacion(lista,articulos, precios):
    recaudacion_total_pba = 0
    recaudacion_total_neuquen = 0
    recaudacion_total_jujuy = 0
    
    for i in range(len(lista)):
        deposito = lista[i][0]
        tipo = lista[i][1]
        cantidad = lista[i][2]
        for h in range(len(articulos)):
            if deposito == "pba":
                if tipo == articulos[h]:
                    recaudacion_total_pba += (precios[h] * cantidad)
            elif deposito == "neuquen":
                if tipo == articulos[h]:
                    recaudacion_total_neuquen += (precios[h] * cantidad)
            elif deposito == "jujuy":
                if tipo == articulos[h]:
                    recaudacion_total_jujuy += (precios[h] * cantidad)


    if recaudacion_total_pba > recaudacion_total_jujuy and recaudacion_total_pba > recaudacion_total_neuquen:
        print(f"El deposito que mas dinero recaudo fue: PBA")
    if recaudacion_total_jujuy > recaudacion_total_neuquen and recaudacion_total_jujuy > recaudacion_total_pba:
        print(f"El deposito que mas dinero recaudo fue: JUJUY")
    if recaudacion_total_neuquen > recaudacion_total_pba and recaudacion_total_neuquen > recaudacion_total_jujuy:
        print(f"El deposito que mas dinero recaudo fue: NEUQUEN")     

    print(f"Jujuy recaudo: {recaudacion_total_jujuy}")
    print(f"Pba recaudo: {recaudacion_total_pba}")
    print(f"Neuquen recaudo: {recaudacion_total_neuquen}")