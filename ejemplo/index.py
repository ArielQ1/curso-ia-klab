import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

datos = pd.read_csv('./Iris.csv')
for columna in datos.select_dtypes(include="number").columns:
    print(f" ------- Columna: {columna}")
    media = np.mean(datos[columna])
    mediana = np.median(datos[columna])
    desviacion = np.std(datos[columna])
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Desviación estándar: {desviacion}")

