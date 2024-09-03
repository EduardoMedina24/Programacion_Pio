from cliente import Cliente, guardar_clientes, cargar_clientes, buscar_cliente, eliminar_cliente

# Crear algunos clientes
cliente1 = Cliente("Juan Pérez", "juan@example.com")
cliente2 = Cliente("Ana Gómez", "ana@example.com")

# Guardar clientes en un archivo
clientes = [cliente1, cliente2]
guardar_clientes(clientes)  # No es necesario pasar la ruta del archivo

# Cargar clientes desde el archivo
clientes_cargados = cargar_clientes()  # No es necesario pasar la ruta del archivo
for cliente in clientes_cargados:
    print(cliente.mostrar_info())

# Buscar un cliente
criterio_busqueda = "Juan Pérez"  # Cambia esto por el criterio que desees usar
cliente_buscado = buscar_cliente(clientes_cargados, criterio_busqueda)
if cliente_buscado:
    print("Cliente encontrado:", cliente_buscado.mostrar_info())
else:
    print("Cliente no encontrado.")

# Eliminar un cliente
criterio_eliminacion = "Ana Gómez"  # Cambia esto por el criterio que desees usar
if eliminar_cliente(clientes_cargados, criterio_eliminacion):
    print("Cliente eliminado con éxito.")
else:
    print("Cliente no encontrado para eliminar.")

# Guardar los cambios después de eliminar
guardar_clientes(clientes_cargados)  # No es necesario pasar la ruta del archivo
