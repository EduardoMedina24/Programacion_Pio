import sys
from clientes.main_cliente import main as gestionar_clientes
from paquetes.main_paquetes import main as gestionar_paquetes
from vuelos.main_reservas_vuelo import main as gestionar_vuelos
from hoteles.main_reservas_hotel import main as gestionar_hoteles
from facturas.main_facturas import main as gestionar_facturas

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Gestión de Clientes")
    print("2. Gestión de Paquetes Turísticos")
    print("3. Gestión de Reservas de Vuelos")
    print("4. Gestión de Reservas de Hoteles")
    print("5. Gestión de Facturación")
    print("6. Salir")

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_clientes()
        elif opcion == "2":
            gestionar_paquetes()
        elif opcion == "3":
            gestionar_vuelos()
        elif opcion == "4":
            gestionar_hoteles()
        elif opcion == "5":
            gestionar_facturas()
        elif opcion == "6":
            print("Saliendo del programa.")
            sys.exit()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()