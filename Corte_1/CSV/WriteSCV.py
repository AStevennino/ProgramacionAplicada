import csv

# Lista de datos fijos: cada elemento es una persona con nombre y edad
personas = [
    ["Nombre", "Edad"],  # Encabezado
    ["Ana", 25],
    ["Luis", 30],
    ["María", 22],
    ["Carlos", 28]
]

# Abrir (o crear) el archivo CSV en modo escritura
with open("personas.csv", mode="w", newline="") as archivo:
    escritor = csv.writer(archivo)
    
    # Escribir todas las filas en el archivo
    escritor.writerows(personas)
