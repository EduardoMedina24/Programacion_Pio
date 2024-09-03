from .gestion_paquetes import guardar_paquetes, cargar_paquetes, buscar_paquete, eliminar_paquete
from .paquete_turistico import PaqueteTuristico

def mostrar_menu_paquetes():
    print("\n--- Menú de Gestión de Paquetes Turísticos ---")
    print("1. Crear un nuevo paquete turístico")
    print("2. Consultar un paquete turístico")
    print("3. Modificar un paquete turístico")
    print("4. Eliminar un paquete turístico")
    print("5. Mostrar todos los paquetes turísticos")
    print("6. Salir")

def crear_paquete(paquetes):
    nombre = input("Ingrese el nombre del paquete: ")
    descripcion = input("Ingrese la descripción del paquete: ")
    precio = float(input("Ingrese el precio del paquete: "))
    destinos = input("Ingrese los destinos (separados por comas): ").split(',')
    paquete = PaqueteTuristico(nombre, descripcion, precio, [destino.strip() for destino in destinos])
    paquetes.append(paquete)
    print("Paquete turístico creado con éxito.")

def modificar_paquete(paquetes):
    nombre = input("Ingrese el nombre del paquete a modificar: ")
    paquete = buscar_paquete(paquetes, nombre)
    if paquete:
        nuevo_nombre = input("Ingrese el nuevo nombre del paquete (presione enter para mantener el actual): ")
        nueva_descripcion = input("Ingrese la nueva descripción (presione enter para mantener la actual): ")
        nuevo_precio = input("Ingrese el nuevo precio (presione enter para mantener el actual): ")
        nuevos_destinos = input("Ingrese los nuevos destinos (separados por comas, presione enter para mantener los actuales): ")

        paquete.actualizar_info(
            nombre=nuevo_nombre if nuevo_nombre else None,
            descripcion=nueva_descripcion if nueva_descripcion else None,
            precio=float(nuevo_precio) if nuevo_precio else None,
            destinos=[destino.strip() for destino in nuevos_destinos.split(',')] if nuevos_destinos else None
        )
        print("Paquete turístico actualizado con éxito.")
    else:
        print("Paquete no encontrado.")

def consultar_paquete(paquetes):
    nombre = input("Ingrese el nombre del paquete a consultar: ")
    paquete = buscar_paquete(paquetes, nombre)
    if paquete:
        print(paquete.mostrar_info())
    else:
        print("Paquete no encontrado.")

def eliminar_paquete_menu(paquetes):
    nombre = input("Ingrese el nombre del paquete a eliminar: ")
    if eliminar_paquete(paquetes, nombre):
        print("Paquete eliminado con éxito.")
    else:
        print("Paquete no encontrado.")

def mostrar_todos_los_paquetes(paquetes):
    if not paquetes:
        print("No hay paquetes turísticos registrados.")
    else:
        for paquete in paquetes:
            print(paquete.mostrar_info())

def main():
    archivo = "data/paquetes.json"
    paquetes = cargar_paquetes(archivo)

    while True:
        mostrar_menu_paquetes()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_paquete(paquetes)
        elif opcion == "2":
            consultar_paquete(paquetes)
        elif opcion == "3":
            modificar_paquete(paquetes)
        elif opcion == "4":
            eliminar_paquete_menu(paquetes)
        elif opcion == "5":
            mostrar_todos_los_paquetes(paquetes)
        elif opcion == "6":
            guardar_paquetes(paquetes, archivo)
            print("Cambios guardados. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
