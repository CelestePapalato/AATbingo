[![Build Status](https://travis-ci.org/CelestePapalato/AATbingo.svg?branch=master)](https://travis-ci.org/CelestePapalato/AATbingo)

# Bingo

Generador de cartón de bingo en Python 3.8.2. Escrito para la materia Adaptación al Ambiente de Trabajo del Instituto Politécnico Superior "Gral. San Martín". Celeste Papalato 6to Informática, 2020.

## Reglas que hacen que un cartón sea considerado válido:

- Los números del carton se encuentran en el rango 1 a 90.
- Cada columna de un carton (contando de izquierda a derecha) contiene numeros que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- No hay números repetidos en el carton.
- Cada fila de un carton tiene exactamente 5 celdas ocupadas.
- Cada carton es una matrix de 3 x 9.
- Cada carton tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada carton debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.

## Usos

Para clonar el repositorio:
```
git clone https://github.com/CelestePapalato/AATbingo
```

Para ejecutar el programa:
```
$ python src/bingo.py
```
Para distribuciones basadas en debian, se debe usar ```python3```

Para informarse sobre cómo instalar o actualizar Python, visite https://www.python.org/

## Ejemplo de salida y formato
```
$ python src/bingo.py
4 0 21 36 0 0 67 71 0
8 0 27 0 42 0 69 0 87
0 10 0 39 0 57 0 74 90
```
