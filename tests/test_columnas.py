from src.bingo import carton

def test_arr_abj():
    mi_carton = (
        (1,2,4,1,7,5,2,1,3),
        (2,3,5,4,8,6,5,7,4),
        (3,6,7,6,9,9,7,8,9),
    )
    for columna in range(0, 9):
        for fila in range(0, 2):
            celda = mi_carton[fila][columna]
            celda_siguiente = mi_carton[fila + 1][columna]
            assert celda < celda_siguiente

def test_empty_row():
    mi_carton = (
        (1,1,0,1,1,1,1,0,1),
        (0,0,1,1,0,1,0,1,0),
        (0,1,0,0,1,0,0,1,1)
    )
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            x = mi_carton[fila][columna] + x
        assert x != 0

def test_row_ocupadas():
    mi_carton = (
        (1,1,0,1,1,1,1,0,1),
        (0,0,1,1,0,1,0,1,0),
        (0,1,0,0,1,0,0,1,1)
    )
    for columna in range(0, 9):
        x = 0
        for fila in range(0, 3):
            if (mi_carton[fila][columna] != 0):
                x = x + 1
        assert x < 3
