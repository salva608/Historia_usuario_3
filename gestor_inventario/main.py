from archivo_csv import crear_csv, agregar_line, leer_line


inventario = []


def registrar_producto():

    while True:
        try:
            nombre = str(input("Ingresa el nombre del producto: "))
            precio = float(input("Ingresa el precio: "))
            cantidad = int(input("Ingresa la cantidad: "))

            if precio < 0 or cantidad < 0:
                print("no se permiten valores negativos")
                continue

            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            inventario.append(producto)
            print("Producto registrado.")
            break
        except ValueError:
            print("ingresa el valor indicado (precio o cantidad)")

def mostrar_producto():

    if not inventario:
        print("Inventario vacío")
    else:
        print("Lista de productos:")
        for p in inventario:
            print(p)


def buscar_producto():

    nombre_buscar = input("Ingresa el nombre del producto a buscar: ")
    encontrado = False

    for producto in inventario:
        if producto["nombre"] == nombre_buscar:
            print(producto)
            encontrado = True

    if not encontrado:
        print("Producto no encontrado.")



def editar_producto():

    nombre_editar = input("Ingresa el nombre del producto a editar: ")
    for p in inventario:
        if p["nombre"] == nombre_editar:
            print("Producto encontrado:", p)
            try:
                p["nombre"] = input("Nuevo nombre: ")
                p["precio"] = float(input("Nuevo precio: "))
                p["cantidad"] = int(input("Nueva cantidad: "))
                print("Producto editado.")
            except ValueError:
                print("Valores inválidos")
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

    if not inventario:    
        print("inventario vacío")
        return
    
    
    unidades = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)
    peoducto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("Unidades totales:", unidades)
    print("Valor total:", valor_total)
    print("Producto más peoducto_mas_caro:", peoducto_mas_caro["nombre"], "-", peoducto_mas_caro["precio"])
    print("Mayor producto_mayor_stock:", producto_mayor_stock["nombre"], "-", producto_mayor_stock["cantidad"])


def guardar_csv_menu():
    crear_csv("inventario.csv", ["nombre", "precio", "cantidad"])
    for p in inventario:
        agregar_line("inventario.csv", [p["nombre"], p["precio"], p["cantidad"]])
    print("CSV guardado.")

def cargar_csv():
    global inventario
    ruta = input("Nombre del archivo CSV: ")
    datos = leer_line(ruta)

    if not datos:
        print("No hay datos para cargar")
        return

    op = input("¿Sobrescribir inventario? (S/N): ").upper()

    if op == "S":
        inventario = datos
    else:
        inventario.extend(datos)

    print("CSV cargado correctamente.")


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
