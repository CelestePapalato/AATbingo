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
