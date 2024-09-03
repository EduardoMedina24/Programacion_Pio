class PaqueteTuristico:
    def __init__(self, nombre, descripcion, precio, destinos):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.destinos = destinos

    def mostrar_info(self):
        return (f"Paquete: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Precio: ${self.precio}\n"
                f"Destinos: {', '.join(self.destinos)}")

    def actualizar_info(self, nombre=None, descripcion=None, precio=None, destinos=None):
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if precio:
            self.precio = precio
        if destinos:
            self.destinos = destinos
