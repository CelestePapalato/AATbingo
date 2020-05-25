from src.bingo import carton
from src.bingo import validar_quince_numeros

def test_contar_celdas_ocupadas():
    carton = (
        (1,0,1,0,0,1,0,0,1),
        (1,0,0,1,0,0,1,0,1),
        (1,0,0,0,1,0,0,1,1),
    )
    assert validar_quince_numeros(carton) == True

def test_contar_celdas_1():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador >= 15

def test_contar_celdas_2():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            contador = contador + celda
    assert contador <= 15

def test_contar_celdas_3():
    mi_carton = carton()
    fila1 = mi_carton[0]
    fila2 = mi_carton[1]
    fila3 = mi_carton[2]
    i = 0
    for x, y, z in zip(fila1, fila2, fila3):
        if( x == 1 or y ==1 or z == 1 ):
            i += 1
    assert i == 9

def test_celdas_repetidas():
    mi_carton = (
        (1,2,3,15,16,4,5,6,17),
        (18,19,10,20,21,22,23,7,24),
        (8,25,26,27,9,28,12,13,14),
    )
    for fila in range(0, 3):
        for columna in range(0, 9):
            celda = mi_carton[fila][columna]
            aux = columna + 1
            if columna == 9:
                aux = 0
            for d_fila in range (fila, 3):
                for d_columna in range (aux, 9):
                    d_celda = mi_carton[d_fila][d_columna]
                    assert celda != d_celda
                aux = 0
