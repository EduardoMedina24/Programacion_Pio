from .gestion_facturas import (guardar_facturas, cargar_facturas, buscar_factura, eliminar_factura)
from .factura import Factura
from datetime import datetime


def mostrar_menu_facturas():
    print("\n--- Menú de Gestión de Facturas ---")
    print("1. Crear una nueva factura")
    print("2. Consultar una factura")
    print("3. Modificar una factura")
    print("4. Eliminar una factura")
    print("5. Mostrar todas las facturas")
    print("6. Salir")

def crear_factura(facturas):
    numero_factura = input("Ingrese el número de factura: ")
    cliente = input("Ingrese el nombre del cliente: ")
    descripcion = input("Ingrese la descripción de la factura: ")
    monto_total = input("Ingrese el monto total: ")
    fecha_emision = input("Ingrese la fecha de emisión (YYYY-MM-DD): ")
    
    
    try:
        fecha_emision = datetime.strptime(fecha_emision, "%Y-%m-%d").date()
    except ValueError:
        print("Fecha inválida. Use el formato YYYY-MM-DD.")
        return

    factura = Factura(numero_factura, cliente, descripcion, monto_total, fecha_emision)
    facturas.append(factura)
    print("Factura creada con éxito.")

def modificar_factura(facturas):
    numero_factura = input("Ingrese el número de factura a modificar: ")
    factura = buscar_factura(facturas, numero_factura)
    if factura:
        nuevo_cliente = input("Ingrese el nuevo nombre del cliente (presione enter para mantener el actual): ")
        nueva_descripcion = input("Ingrese la nueva descripción (presione enter para mantener la actual): ")
        nuevo_monto_total = input("Ingrese el nuevo monto total (presione enter para mantener el actual): ")
        nueva_fecha_emision = input("Ingrese la nueva fecha de emisión (YYYY-MM-DD, presione enter para mantener la actual): ")

        
        try:
            nueva_fecha_emision = datetime.strptime(nueva_fecha_emision, "%Y-%m-%d").date() if nueva_fecha_emision else None
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        factura.actualizar_info(
            cliente=nuevo_cliente if nuevo_cliente else None,
            descripcion=nueva_descripcion if nueva_descripcion else None,
            monto_total=nuevo_monto_total if nuevo_monto_total else None,
            fecha_emision=nueva_fecha_emision if nueva_fecha_emision else None
        )
        print("Factura actualizada con éxito.")
    else:
        print("Factura no encontrada.")

def consultar_factura(facturas):
    numero_factura = input("Ingrese el número de factura a consultar: ")
    factura = buscar_factura(facturas, numero_factura)
    if factura:
        print(factura.mostrar_info())
    else:
        print("Factura no encontrada.")

def eliminar_factura_menu(facturas):
    numero_factura = input("Ingrese el número de factura a eliminar: ")
    if eliminar_factura(facturas, numero_factura):
        print("Factura eliminada con éxito.")
    else:
        print("Factura no encontrada.")

def mostrar_todas_las_facturas(facturas):
    if not facturas:
        print("No hay facturas registradas.")
    else:
        for factura in facturas:
            print(factura.mostrar_info())

def main():
    archivo = "data/facturas.json"
    facturas = cargar_facturas(archivo)

    while True:
        mostrar_menu_facturas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_factura(facturas)
        elif opcion == "2":
            consultar_factura(facturas)
        elif opcion == "3":
            modificar_factura(facturas)
        elif opcion == "4":
            eliminar_factura_menu(facturas)
        elif opcion == "5":
            mostrar_todas_las_facturas(facturas)
        elif opcion == "6":
            guardar_facturas(facturas, archivo)
            print("Cambios guardados. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
