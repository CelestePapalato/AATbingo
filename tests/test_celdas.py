from src.bingo import carton

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
