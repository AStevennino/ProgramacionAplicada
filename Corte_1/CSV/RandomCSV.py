import csv
import random

# Para escribir el archivo
valores = [random.random() for i in range(30)]

with open("valores.csv", mode="w", newline="") as archivo:
    esc = csv.writer(archivo)
    esc.writerows([[valor] for valor in valores])

# Para leer el archivo
with open("valores.csv", mode="r") as archivo:
    leer = csv.reader(archivo)
    for fila in leer:
        print(fila)
