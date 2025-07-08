print("Asignando el valor 5 a la variable a")
a = 5
b = 10
c = a + b
print("Mostrando el resultado de la suma de a + b:")
print("El valor de c es:", c)

# Empiezo a programar algo mas complejo 
print("************* bucle for simple *************")

for i in range(1, 11):
    print("Mostrando el valor actual de i:")
    print(f"El valor de i es: {i}")
    print("Calculando y mostrando el cuadrado de i:")
    print(f"El cuadrado de {i} es: {i+1}")

print("************* bucle for con saltos de 2 en 2 *************")

for i in range(1, 11, 2):
    print("Mostrando valores con saltos de 2 en 2:")
    print(f"El valor de i es: {i}")

print("************* bucle for con saltos negativos *************")

for j in range(10, 5, -2):
    print("Mostrando valores con saltos negativos:")
    print(f"El valor de j es: {j}")

print("************* recorrer listas *************")

print("----------- listas con numeros enteros -----------")
lista1 = [1, 2, 3, 4, 5]
for i in lista1:
    print("Mostrando cada elemento de la lista de números:")
    print(f"El valor de i es: {i}")
print("----------- listas con una string -----------")
listas2 = "ariel"
for i in listas2:
    print("Mostrando cada carácter de la string:")
    print(f"El valor de i es: {i}")

print("************* funciones *************")

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b

print("Probando la función suma:")
print("La suma de 5 y 10 es:", suma(5, 10))
print("Probando la función resta:")
print("La resta de 10 y 5 es:", resta(10, 5))

def multi(a, b):
    return sum([a for i in range(b)])

print("Mostrando el resultado de la multiplicación usando suma repetida:")
print(multi(3, 4))

import numpy 
listanormal = [5, 6, 7, 8]
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

vector = numpy.array(listanormal)
matriz2 = numpy.array(matriz)
print("Mostrando la lista normal:")
print(listanormal)
print("Mostrando el vector de numpy:")
print(vector)
print("Mostrando la matriz normal:")
print(matriz)
print("Mostrando la matriz de numpy:")
print(matriz2)

print("Calculando la media del vector:")
print(numpy.mean(vector))
print("Calculando la media de la matriz:")
print(numpy.mean(matriz2))
print("Calculando la mediana del vector:")
print(numpy.median(vector))
print("Calculando la mediana de la matriz:")
print(numpy.median(matriz2))

print("Calculando la media por columnas:")
print(numpy.mean(matriz2, axis=0))  # Media por columnas
print("Calculando la media por filas:")
print(numpy.mean(matriz2, axis=1))  # Media por filas