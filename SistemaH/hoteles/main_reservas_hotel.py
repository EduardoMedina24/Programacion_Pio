from hoteles.gestion_reservas_hotel import (guardar_reservas, cargar_reservas, buscar_reserva, eliminar_reserva)
from hoteles.reserva_hotel import ReservaHotel
from datetime import datetime

def mostrar_menu_reservas_hotel():
    """
    Muestra el menú principal para la gestión de reservas de hoteles.
    """
    print("\n--- Menú de Gestión de Reservas de Hoteles ---")
    print("1. Crear una nueva reserva de hotel")
    print("2. Consultar una reserva de hotel")
    print("3. Modificar una reserva de hotel")
    print("4. Eliminar una reserva de hotel")
    print("5. Mostrar todas las reservas de hotel")
    print("6. Salir")

def crear_reserva(reservas):
    """
    Crea una nueva reserva de hotel y la añade a la lista.
    
    :param reservas: Lista de reservas en la que añadir la nueva reserva.
    """
    codigo_reserva = input("Código de Reserva: ")
    cliente = input("Cliente: ")
    hotel = input("Hotel: ")
    fecha_reserva = input("Fecha de Reserva (YYYY-MM-DD): ")
    fecha_checkin = input("Fecha de Check-in (YYYY-MM-DD): ")
    fecha_checkout = input("Fecha de Check-out (YYYY-MM-DD): ")

    try:
        fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        fecha_checkin = datetime.strptime(fecha_checkin, "%Y-%m-%d").date()
        fecha_checkout = datetime.strptime(fecha_checkout, "%Y-%m-%d").date()
        
        reserva = ReservaHotel(codigo_reserva, cliente, hotel, fecha_reserva, fecha_checkin, fecha_checkout)
        reservas.append(reserva)
        guardar_reservas(reservas, "data/hoteles.json")
        print("Reserva creada con éxito.")
    except ValueError:
        print("Error: La fecha debe estar en formato YYYY-MM-DD.")

def modificar_reserva(reservas):
    """
    Modifica una reserva existente.
    
    :param reservas: Lista de reservas.
    """
    codigo_reserva = input("Código de Reserva a modificar: ")
    reserva = buscar_reserva(reservas, codigo_reserva)
    
    if reserva:
        print("Reserva encontrada.")
        cliente = input(f"Nuevo Cliente (dejar en blanco para no cambiar): ")
        hotel = input(f"Nuevo Hotel (dejar en blanco para no cambiar): ")
        fecha_reserva = input(f"Nueva Fecha de Reserva (dejar en blanco para no cambiar, formato YYYY-MM-DD): ")
        fecha_checkin = input(f"Nueva Fecha de Check-in (dejar en blanco para no cambiar, formato YYYY-MM-DD): ")
        fecha_checkout = input(f"Nueva Fecha de Check-out (dejar en blanco para no cambiar, formato YYYY-MM-DD): ")

        if cliente:
            reserva.cliente = cliente
        if hotel:
            reserva.hotel = hotel
        if fecha_reserva:
            reserva.fecha_reserva = datetime.strptime(fecha_reserva, "%Y-%m-%d").date()
        if fecha_checkin:
            reserva.fecha_checkin = datetime.strptime(fecha_checkin, "%Y-%m-%d").date()
        if fecha_checkout:
            reserva.fecha_checkout = datetime.strptime(fecha_checkout, "%Y-%m-%d").date()
        
        guardar_reservas(reservas, "data/hoteles.json")
        print("Reserva modificada con éxito.")
    else:
        print("Reserva no encontrada.")

def consultar_reserva(reservas):
    """
    Consulta una reserva por código y muestra la información.
    
    :param reservas: Lista de reservas.
    """
    codigo_reserva = input("Código de Reserva a consultar: ")
    reserva = buscar_reserva(reservas, codigo_reserva)
    
    if reserva:
        print(reserva.mostrar_info())
    else:
        print("Reserva no encontrada.")

def eliminar_reserva_menu(reservas):
    """
    Elimina una reserva por código.
    
    :param reservas: Lista de reservas.
    """
    codigo_reserva = input("Código de Reserva a eliminar: ")
    if eliminar_reserva(reservas, codigo_reserva):
        guardar_reservas(reservas, "data/hoteles.json")
        print("Reserva eliminada con éxito.")
    else:
        print("Reserva no encontrada.")

def mostrar_todas_las_reservas(reservas):
    """
    Muestra todas las reservas registradas.
    
    :param reservas: Lista de reservas.
    """
    if reservas:
        for reserva in reservas:
            print(reserva.mostrar_info())
    else:
        print("No hay reservas registradas.")

def main():
    """
    Función principal para ejecutar el menú de gestión de reservas de hoteles.
    """
    reservas = cargar_reservas("data/hoteles.json")
    
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
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
