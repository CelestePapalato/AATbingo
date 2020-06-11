from tests.test_1_a_90 import carton

def test_arr_abj():
    mi_carton = carton
    for columna in range(0, 9):
        for fila in range(0, 2):
            celda = mi_carton[fila][columna]
            for d_fila in range (fila, 3):
                celda_siguiente = mi_carton[d_fila][columna]
                if(celda_siguiente != 0):
                    assert celda <= celda_siguiente

def test_empty_row():
    mi_carton = carton
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            x = mi_carton[fila][columna] + x
        assert x != 0

def test_row_ocupadas():
    mi_carton = carton
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        assert x < 3

def test_row_1():
    mi_carton = carton
    ocupadas_con_uno = 0
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        if (x == 1):
            ocupadas_con_uno = ocupadas_con_uno + 1
    assert ocupadas_con_uno == 3
