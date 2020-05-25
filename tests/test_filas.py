from src.bingo import carton

def test_contar_filas():
    mi_carton = carton()
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
    assert bandera == 1

def test_izq_der():
    mi_carton = (
        (1,2,3,4,5,6,7,8,9),
        (1,2,3,4,5,6,7,8,9),
        (1,2,3,4,5,6,7,8,9),
    )
    a = 1
    for fila in range(0, 3):
        for columna in range(0, 8):
            celda = mi_carton[fila][columna]
            celda_siguiente = mi_carton[fila][columna + 1]
            assert celda < celda_siguiente

def test_arr_abj():
    mi_carton = (
        (1,2,4,1,7,5,2,1,3),
        (2,3,5,4,8,6,5,7,4),
        (3,6,7,6,9,9,7,8,9),
    )
    a = 1
    for columna in range(0, 9):
        for fila in range(0, 2):
            celda = mi_carton[fila][columna]
            celda_siguiente = mi_carton[fila + 1][columna]
            assert celda < celda_siguiente
