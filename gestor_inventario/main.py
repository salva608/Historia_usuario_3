from archivo_csv import crear_csv, agregar_line


inventario = []


def registrar_producto():

    while True:
        try:
            nombre = str(input("Ingresa el nombre del producto: "))
            print(nombre.replace("",""))
            precio = float(input("Ingresa el precio: "))
            cantidad = int(input("Ingresa la cantidad: "))   

            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)
            print("Producto registrado.")
            break
        except ValueError:
            print("ingresa el valor indicado (precio o cantidad)")

def mostrar_producto():

    buscar=(input("Ingresa el nombre del producto a buscar: "))

    print (str(f"Aqui tienes tus productos: {buscar}"))

def buscar_producto():

    nombre_buscar = (input("Ingresa el nombre del producto a editar: "))
    for buscar in inventario:
        if buscar["nombre"] == nombre_buscar:
            print(f"Producto encontrado. {nombre_buscar}")
    print("Producto no encontrado.")

def editar_producto():

    nombre_editar = input("Ingresa el nombre del producto a editar: ")
    for p in inventario:
        if p["nombre"] == nombre_editar:
            print(f"Producto encontrado. {inventario}")
            p["nombre"] = input("Nuevo nombre: ")
            p["precio"] = float(input("Nuevo precio: "))
            p["cantidad"] = int(input("Nueva cantidad: "))
            print("Producto editado.")
            return
    print("Producto no encontrado.")


def eliminar_producto():
    nombre_buscar = input("Nombre del producto a eliminar: ")
    for p in inventario:
        if p["nombre"] == nombre_buscar:
            inventario.remove(p)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")

def cargar_estadistica():
    print


def guardar_csv_menu():
    crear_csv("inventario.csv", ["nombre", "precio", "cantidad"])
    for p in inventario:
        agregar_line("inventario.csv", [p["nombre"], p["precio"], p["cantidad"]])
    print("CSV guardado.")

def cargar_csv():
    print

while True:
    print("MENU")
    print("1. Agregar producto")
    print("2. Mostar producto")
    print("3. Buscar producto")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadistica")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            registrar_producto()
        case "2":
            mostrar_producto()
        case "3":
            buscar_producto()
        case "4":
            editar_producto()
        case "5":
            eliminar_producto()
        case "6":
            cargar_estadistica()
        case "7":
            guardar_csv_menu()
        case "8":
            cargar_csv()
        case "9":
            break
        case _:
            print("Opción inválida.")
