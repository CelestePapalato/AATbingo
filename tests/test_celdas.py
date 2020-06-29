from tests.test_1_a_90 import carton
from src.funciones import validar_quince_numeros

def test_contar_celdas_ocupadas():
    mi_carton = carton
    assert validar_quince_numeros(carton) == True

def test_contar_celdas_1():
    mi_carton = carton
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if(celda != 0):
                contador += 1
    assert contador >= 15

def test_contar_celdas_2():
    mi_carton = carton
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if(celda != 0):
                contador += 1
    assert contador <= 15

def test_contar_celdas_3():
    mi_carton = carton
    fila1 = mi_carton[0]
    fila2 = mi_carton[1]
    fila3 = mi_carton[2]
    i = 0
    for x, y, z in zip(fila1, fila2, fila3):
        if( x != 0 or y != 0 or z != 0 ):
            i += 1
    assert i == 9

def test_celdas_repetidas():
    mi_carton = carton
    for fila in range(0, 3):
        for columna in range(0, 9):
            celda = mi_carton[fila][columna]
            if(celda != 0):
                aux = columna + 1
                for d_fila in range (fila, 3):
                    for d_columna in range (aux, 9):
                        d_celda = mi_carton[d_fila][d_columna]
                        if(d_celda != 0):
                            assert celda != d_celda
                    aux = 0
