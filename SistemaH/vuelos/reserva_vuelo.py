class ReservaVuelo:
    def __init__(self, codigo_reserva, cliente, vuelo, fecha_reserva, fecha_salida, fecha_llegada):
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada

    def mostrar_info(self):
        """
        Devuelve la información de la reserva en un formato legible.
        """
        return (f"Código de Reserva: {self.codigo_reserva}\n"
                f"Cliente: {self.cliente}\n"
                f"Vuelo: {self.vuelo}\n"
                f"Fecha de Reserva: {self.fecha_reserva}\n"
                f"Fecha de Salida: {self.fecha_salida}\n"
                f"Fecha de Llegada: {self.fecha_llegada}")
