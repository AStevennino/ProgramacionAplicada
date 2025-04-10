import csv

# Abrir el archivo CSV en modo lectura
with open("personas.csv", mode="r") as archivo:
    lector = csv.reader(archivo)
    
    # Recorrer cada fila del archivo
    for fila in lector:
        print(fila)
