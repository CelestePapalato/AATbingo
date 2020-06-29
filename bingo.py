from src.funciones import *

def imprimir():
    carton = generar_carton()
    part1 = list(carton[0])
    part2 = list(carton[1])
    part3 = list(carton[2])
    print(part1[0], part1[1], part1[2], part1[3], part1[4], part1[5], part1[6], part1[7], part1[8])
    print(part2[0], part2[1], part2[2], part2[3], part2[4], part2[5], part2[6], part2[7], part2[8])
    print(part3[0], part3[1], part3[2], part3[3], part3[4], part3[5], part3[6], part3[7], part3[8])

imprimir()
