import csv

def crear_csv(name_archivo, encabezado):
    with open(name_archivo, "w", newline="") as file:
        writer =csv.writer(file)
        writer.writerow(encabezado)

def agregar_line(name_archivo, datos):
    with open(name_archivo, "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(datos)

def leer_line (name_archivo, leer):
    with open(name_archivo, "r") as file:
        file