import csv

def crear_csv(name_archivo, encabezado):
    with open(name_archivo, "w", newline="") as file:
        writer =csv.writer(file)
        writer.writerow(encabezado)

def agregar_line(name_archivo, datos):
    with open(name_archivo, "a", newline="") as file:
        writer=csv.writer(file)
        writer.writerow(datos)

def leer_line(name_archivo):
    productos = []

    try:
        with open(name_archivo, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for fila in reader:
                productos.append({
                    "nombre": fila[0],
                    "precio": float(fila[1]),
                    "cantidad": int(fila[2])
                })
        return productos
    except:
        print("Error al leer el archivo")
        return []
