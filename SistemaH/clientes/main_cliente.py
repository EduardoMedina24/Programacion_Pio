from .cliente import Cliente, guardar_clientes, cargar_clientes, buscar_cliente, eliminar_cliente

def mostrar_menu():
    print("\n--- Menú de Gestión de Clientes ---")
    print("1. Registrar un nuevo cliente")
    print("2. Consultar un cliente")
    print("3. Eliminar un cliente")
    print("4. Mostrar todos los clientes")
    print("5. Salir")

def registrar_cliente(clientes):
    nombre = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el email del cliente: ")
    cliente = Cliente(nombre, email)
    clientes.append(cliente)
    print("Cliente registrado con éxito.")

def consultar_cliente(clientes):
    criterio = input("Ingrese el nombre o email del cliente a consultar: ")
    cliente = buscar_cliente(clientes, criterio)
    if cliente:
        print("Cliente encontrado:", cliente.mostrar_info())
    else:
        print("Cliente no encontrado.")

def eliminar_cliente_menu(clientes):
    criterio = input("Ingrese el nombre o email del cliente a eliminar: ")
    if eliminar_cliente(clientes, criterio):
        print("Cliente eliminado con éxito.")
    else:
        print("Cliente no encontrado.")

def mostrar_todos_los_clientes(clientes):
    if not clientes:
        print("No hay clientes registrados.")
    else:
        for cliente in clientes:
            print(cliente.mostrar_info())

def main():
    clientes = cargar_clientes()   

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente(clientes)
        elif opcion == "2":
            consultar_cliente(clientes)
        elif opcion == "3":
            eliminar_cliente_menu(clientes)
        elif opcion == "4":
            mostrar_todos_los_clientes(clientes)
        elif opcion == "5":
            guardar_clientes(clientes)  
            print("Cambios guardados. Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
