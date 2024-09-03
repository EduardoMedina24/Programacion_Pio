from vuelos.gestion_reservas_vuelo import (guardar_reservas, cargar_reservas, 
                                           buscar_reserva, eliminar_reserva)
from vuelos.reserva_vuelo import ReservaVuelo
from datetime import datetime

def mostrar_menu_reservas_vuelo():
    print("\n--- Menú de Gestión de Reservas de Vuelos ---")
    print("1. Crear una nueva reserva de vuelo")
    print("2. Consultar una reserva de vuelo")
    print("3. Modificar una reserva de vuelo")
    print("4. Eliminar una reserva de vuelo")
    print("5. Mostrar todas las reservas de vuelo")
    print("6. Salir")

def crear_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva: ")
    cliente = input("Ingrese el nombre del cliente: ")
    vuelo = input("Ingrese el número de vuelo: ")
    fecha_reserva = input("Ingrese la fecha de reserva (YYYY-MM-DD): ")
    fecha_salida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
    fecha_llegada = input("Ingrese la fecha de llegada (YYYY-MM-DD): ")

    # Validar fechas
    try:
        fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        fecha_salida = datetime.strptime(fecha_salida, "%Y-%m-%d").date()
        fecha_llegada = datetime.strptime(fecha_llegada, "%Y-%m-%d").date()
    except ValueError:
        print("Fecha inválida. Use el formato YYYY-MM-DD.")
        return

    reserva = ReservaVuelo(codigo_reserva, cliente, vuelo, fecha_reserva, fecha_salida, fecha_llegada)
    reservas.append(reserva)
    print("Reserva de vuelo creada con éxito.")

def modificar_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva a modificar: ")
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        nuevo_cliente = input("Ingrese el nuevo nombre del cliente (presione enter para mantener el actual): ")
        nuevo_vuelo = input("Ingrese el nuevo número de vuelo (presione enter para mantener el actual): ")
        nueva_fecha_reserva = input("Ingrese la nueva fecha de reserva (YYYY-MM-DD, presione enter para mantener la actual): ")
        nueva_fecha_salida = input("Ingrese la nueva fecha de salida (YYYY-MM-DD, presione enter para mantener la actual): ")
        nueva_fecha_llegada = input("Ingrese la nueva fecha de llegada (YYYY-MM-DD, presione enter para mantener la actual): ")

        # Validar fechas
        try:
            nueva_fecha_reserva = datetime.strptime(nueva_fecha_reserva, "%Y-%m-%d").date() if nueva_fecha_reserva else None
            nueva_fecha_salida = datetime.strptime(nueva_fecha_salida, "%Y-%m-%d").date() if nueva_fecha_salida else None
            nueva_fecha_llegada = datetime.strptime(nueva_fecha_llegada, "%Y-%m-%d").date() if nueva_fecha_llegada else None
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        reserva.actualizar_info(
            cliente=nuevo_cliente if nuevo_cliente else None,
            vuelo=nuevo_vuelo if nuevo_vuelo else None,
            fecha_reserva=nueva_fecha_reserva if nueva_fecha_reserva else None,
            fecha_salida=nueva_fecha_salida if nueva_fecha_salida else None,
            fecha_llegada=nueva_fecha_llegada if nueva_fecha_llegada else None
        )
        print("Reserva de vuelo actualizada con éxito.")
    else:
        print("Reserva no encontrada.")

def consultar_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva a consultar: ")
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        print(reserva.mostrar_info())
    else:
        print("Reserva no encontrada.")

def eliminar_reserva_menu(reservas):
    codigo_reserva = input("Ingrese el código de reserva a eliminar: ")
    if eliminar_reserva(reservas, codigo_reserva):
        print("Reserva eliminada con éxito.")
    else:
        print("Reserva no encontrada.")

def mostrar_todas_las_reservas(reservas):
    if not reservas:
        print("No hay reservas de vuelo registradas.")
    else:
        for reserva in reservas:
            print(reserva.mostrar_info())

def main():
    archivo = "data/reservas_vuelo.json"
    reservas = cargar_reservas(archivo)

    while True:
        mostrar_menu_reservas_vuelo()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_reserva(reservas)
        elif opcion == "2":
            consultar_reserva(reservas)
        elif opcion == "3":
            modificar_reserva(reservas)
        elif opcion == "4":
            eliminar_reserva_menu(reservas)
        elif opcion == "5":
            mostrar_todas_las_reservas(reservas)
        elif opcion == "6":
            guardar_reservas(reservas, archivo)
            print("Cambios guardados. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
