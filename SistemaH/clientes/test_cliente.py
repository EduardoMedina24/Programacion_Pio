from cliente import Cliente, guardar_clientes, cargar_clientes, buscar_cliente, eliminar_cliente


cliente1 = Cliente("Juan Pérez", "juan@example.com")
cliente2 = Cliente("Ana Gómez", "ana@example.com")


clientes = [cliente1, cliente2]
guardar_clientes(clientes)


clientes_cargados = cargar_clientes() 
for cliente in clientes_cargados:
    print(cliente.mostrar_info())


criterio_busqueda = "Juan Pérez"  
cliente_buscado = buscar_cliente(clientes_cargados, criterio_busqueda)
if cliente_buscado:
    print("Cliente encontrado:", cliente_buscado.mostrar_info())
else:
    print("Cliente no encontrado.")


if eliminar_cliente(clientes_cargados, criterio_eliminacion):
    print("Cliente eliminado con éxito.")
else:
    print("Cliente no encontrado para eliminar.")


guardar_clientes(clientes_cargados) 