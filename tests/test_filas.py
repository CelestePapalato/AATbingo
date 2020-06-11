from tests.test_1_a_90 import carton

def test_contar_filas():
    mi_carton = carton
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
    mi_carton = carton
    for fila in range(0, 3):
        for columna in range(0, 8):
            celda = mi_carton[fila][columna]
            if(celda != 0):
                celda_siguiente = mi_carton[fila][columna + 1]
                if(celda_siguiente != 0):
                    assert celda < celda_siguiente

def test_filas_ocupadas():
    mi_carton = carton
    for fila in range(0, 3):
        x = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        assert x == 5

def test_ocupadas_consecutivas():
    mi_carton = carton
    for fila in range(0, 3):
        x = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
            else:
                x = 0
            assert x <= 2

def test_vacias_consecutivas():
    mi_carton = carton
    for fila in range(0, 3):
        x = 0
        for columna in range(0, 9):
            if (mi_carton[fila][columna] == 0):
                x = x + 1
            else:
                x = 0
            assert x <= 2
