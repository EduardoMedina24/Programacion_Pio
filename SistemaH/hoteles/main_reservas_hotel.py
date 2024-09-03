
from hoteles.gestion_reservas_hotel import (guardar_reservas, cargar_reservas,buscar_reserva, eliminar_reserva)

from hoteles.reserva_hotel import ReservaHotel

from datetime import datetime

def mostrar_menu_reservas_hotel():
    print("\n--- Menú de Gestión de Reservas de Hoteles ---")
    print("1. Crear una nueva reserva de hotel")
    print("2. Consultar una reserva de hotel")
    print("3. Modificar una reserva de hotel")
    print("4. Eliminar una reserva de hotel")
    print("5. Mostrar todas las reservas de hotel")
    print("6. Salir")

def crear_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva: ")
    cliente = input("Ingrese el nombre del cliente: ")
    hotel = input("Ingrese el nombre del hotel: ")
    fecha_reserva = input("Ingrese la fecha de reserva (YYYY-MM-DD): ")
    fecha_checkin = input("Ingrese la fecha de check-in (YYYY-MM-DD): ")
    fecha_checkout = input("Ingrese la fecha de check-out (YYYY-MM-DD): ")
    
    # Validar fechas
    try:
        fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        fecha_checkin = datetime.strptime(fecha_checkin, "%Y-%m-%d").date()
        fecha_checkout = datetime.strptime(fecha_checkout, "%Y-%m-%d").date()
    except ValueError:
        print("Fecha inválida. Use el formato YYYY-MM-DD.")
        return

    reserva = ReservaHotel(codigo_reserva, cliente, hotel, fecha_reserva, fecha_checkin, fecha_checkout)
    reservas.append(reserva)
    print("Reserva de hotel creada con éxito.")

def modificar_reserva(reservas):
    codigo_reserva = input("Ingrese el código de reserva a modificar: ")
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        nuevo_cliente = input("Ingrese el nuevo nombre del cliente (presione enter para mantener el actual): ")
        nuevo_hotel = input("Ingrese el nuevo nombre del hotel (presione enter para mantener el actual): ")
        nueva_fecha_reserva = input("Ingrese la nueva fecha de reserva (YYYY-MM-DD, presione enter para mantener la actual): ")
        nueva_fecha_checkin = input("Ingrese la nueva fecha de check-in (YYYY-MM-DD, presione enter para mantener la actual): ")
        nueva_fecha_checkout = input("Ingrese la nueva fecha de check-out (YYYY-MM-DD, presione enter para mantener la actual): ")

        # Validar fechas
        try:
            nueva_fecha_reserva = datetime.strptime(nueva_fecha_reserva, "%Y-%m-%d").date() if nueva_fecha_reserva else None
            nueva_fecha_checkin = datetime.strptime(nueva_fecha_checkin, "%Y-%m-%d").date() if nueva_fecha_checkin else None
            nueva_fecha_checkout = datetime.strptime(nueva_fecha_checkout, "%Y-%m-%d").date() if nueva_fecha_checkout else None
        except ValueError:
            print("Fecha inválida. Use el formato YYYY-MM-DD.")
            return

        reserva.actualizar_info(
            cliente=nuevo_cliente if nuevo_cliente else None,
            hotel=nuevo_hotel if nuevo_hotel else None,
            fecha_reserva=nueva_fecha_reserva if nueva_fecha_reserva else None,
            fecha_checkin=nueva_fecha_checkin if nueva_fecha_checkin else None,
            fecha_checkout=nueva_fecha_checkout if nueva_fecha_checkout else None
        )
        print("Reserva de hotel actualizada con éxito.")
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
        print("No hay reservas de hotel registradas.")
    else:
        for reserva in reservas:
            print(reserva.mostrar_info())

def main():
    archivo = "data/reservas_hotel.json"
    reservas = cargar_reservas(archivo)

    while True:
        mostrar_menu_reservas_hotel()
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
