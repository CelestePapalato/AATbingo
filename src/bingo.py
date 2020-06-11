def validar_quince_numeros(carton):
    celdas = 0
    for fila in carton:
        for celda in fila:
            if celda != 0:
                celdas = celdas + 1

    return celdas == 15

def test_uno_a_noventa(mi_carton):
    contador = 0
    for fila in range(0, 3):
        for columna in range(0, 9):
            celda = mi_carton[fila][columna]
            return (celda >= 0 and celda <= 90)

def test_matrix(mi_carton):
    rows = len(mi_carton)
    if (rows == 3):
        for i in range(0, 3):
            columns = len(mi_carton[i])
            return (columns == 9)
    else:
        return false

def test_contar_celdas_1(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if(celda != 0):
                contador += 1
    return (contador >= 15)

def test_contar_celdas_2(mi_carton):
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if(celda != 0):
                contador += 1
    return (contador <= 15)

def test_contar_celdas_3(mi_carton):
    fila1 = mi_carton[0]
    fila2 = mi_carton[1]
    fila3 = mi_carton[2]
    i = 0
    for x, y, z in zip(fila1, fila2, fila3):
        if( x != 0 or y != 0 or z != 0 ):
            i += 1
    return (i == 9)

def test_celdas_repetidas(mi_carton):
    i = 0
    for fila in range(0, 3):
        for columna in range(0, 9):
            celda = mi_carton[fila][columna]
            if(celda != 0):
                aux = columna + 1
                if columna == 9:
                    aux = 0
                for d_fila in range (fila, 3):
                    for d_columna in range (aux, 9):
                        d_celda = mi_carton[d_fila][d_columna]
                        if(d_celda != 0):
                            if (celda == d_celda):
                                i = 1
                    aux = 0
    return (i == 0)

def test_contar_filas(mi_carton):
    fila1 = mi_carton[0]
    fila2 = mi_carton[1]
    fila3 = mi_carton[2]
    x = 0
    y = 0
    z = 0
    bandera = 0
    for celda in fila1:
        x = x + celda
    for celda in fila2:
        y = y + celda
    for celda in fila3:
        z = z + celda
    if( x > 0 and y > 0 and z > 0):
        bandera = 1
    return (bandera == 1)

def test_izq_der(mi_carton):
    x = 1
    for fila in range(0, 3):
        for columna in range(0, 8):
            celda = mi_carton[fila][columna]
            if(celda != 0):
                celda_siguiente = mi_carton[fila][columna + 1]
                if(celda_siguiente != 0):
                    if (celda > celda_siguiente):
                        x = 0
        return (x == 1)

def test_filas_ocupadas(mi_carton):
    for fila in range(0, 3):
        x = 0
        y = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        if (x != 5):
                y = 1
        x = 0
        return (y == 0)

def test_ocupadas_consecutivas(mi_carton):
    y = 1
    for fila in range(0, 3):
        x = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
            else:
                x = 0
            if (x > 2):
                y = 0
    return (y == 1)

def test_vacias_consecutivas(mi_carton):
    y = 1
    for fila in range(0, 3):
        x = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] == 0):
                x = x + 1
            else:
                x = 0
            if (x > 2):
                y = 0
    return (y == 1)

def test_arr_abj(mi_carton):
    y = 1
    for columna in range(0, 9):
        for fila in range(0, 2):
            celda = mi_carton[fila][columna]
            for d_fila in range (fila, 3):
                celda_siguiente = mi_carton[d_fila][columna]
                if(celda_siguiente != 0):
                    if (celda > celda_siguiente):
                        y = 0
    return (y == 1)

def test_empty_row(mi_carton):
    y = 1
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            x = mi_carton[fila][columna] + x
        if (x == 0):
            y = 0
    return (y == 1)

def test_row_ocupadas(mi_carton):
    y = 1
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        if (x == 3):
            y = 0
    return (y == 1)

def test_row_1(mi_carton):
    ocupadas_con_uno = 0
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        if (x == 1):
            ocupadas_con_uno = ocupadas_con_uno + 1
    return (ocupadas_con_uno == 3)
