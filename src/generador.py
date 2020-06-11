import random
import math
from src.bingo import *

def intentoCarton():
    contador = 0
    carton = [[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]]
    numerosCarton = 0
    intentos_maximos = 0
    while (numerosCarton < 15):
        contador = contador + 1
        if (contador == 50):
            return intentoCarton()

        numero = random.randint(1, 90)

        columna = math.floor(numero / 10)
        if (columna >= 9):
            columna = 8
        huecos = 0
        for i in range(0, 3):
            if (carton[i][columna] == 0):
                huecos = huecos + 1
            if (carton[i][columna] == numero):
                huecos = 0
                break

        if (huecos < 2):
            continue

        fila = 0;
        for j in range(0, 3):
            huecos = 0
            for i in range(0, 9):
                if (carton[fila][i] == 0):
                    huecos = huecos + 1
            if (huecos < 5 or carton[fila][columna] != 0):
                fila = fila + 1
            else:
                break

        if (fila == 3):
            continue

        carton[fila][columna] = numero
        numerosCarton = numerosCarton + 1
        contador = 0


    for x in range(0, 3):
        huecos = 0
        for y in range(0, 9):
            if (carton[x][y] == 0):
                huecos = huecos + 1

        if (huecos == 3):
            return intentoCarton()

    carton1 = tuple(carton[0])
    carton2 = tuple(carton[1])
    carton3 = tuple(carton[2])
    cartonF = (carton1, carton2, carton3)

    if(validar_quince_numeros(cartonF) == False):
        return intentoCarton()
    if(test_uno_a_noventa(cartonF) == False):
        return intentoCarton()
    if(test_matrix(cartonF) == False):
        return intentoCarton()
    if(test_contar_celdas_1(cartonF) == False):
        return intentoCarton()
    if(test_contar_celdas_2(cartonF) == False):
        return intentoCarton()
    if(test_contar_celdas_3(cartonF) == False):
        return intentoCarton()
    if(test_celdas_repetidas(cartonF) == False):
        return intentoCarton()
    if(test_contar_filas(cartonF) == False):
        return intentoCarton()
    if(test_izq_der(cartonF) == False):
        return intentoCarton()
    if(test_filas_ocupadas(cartonF) == False):
        return intentoCarton()
    if(test_ocupadas_consecutivas(cartonF) == False):
        return intentoCarton()
    if(test_vacias_consecutivas(cartonF) == False):
        return intentoCarton()
    if(test_arr_abj(cartonF) == False):
        return intentoCarton()
    if(test_empty_row(cartonF) == False):
        return intentoCarton()
    if(test_row_ocupadas(cartonF) == False):
        return intentoCarton()
    if(test_row_1(cartonF) == False):
        return intentoCarton()

    return cartonF
