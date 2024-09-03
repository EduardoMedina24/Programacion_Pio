from datetime import date

class ReservaVuelo:
    def __init__(self, codigo_reserva, cliente, vuelo, fecha_reserva, fecha_salida, fecha_llegada):
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.vuelo = vuelo
        self.fecha_reserva = fecha_reserva
        self.fecha_salida = fecha_salida
        self.fecha_llegada = fecha_llegada

    def mostrar_info(self):
        info = (
            f"Código de Reserva: {self.codigo_reserva}\n"
            f"Cliente: {self.cliente}\n"
            f"Vuelo: {self.vuelo}\n"
            f"Fecha de Reserva: {self.fecha_reserva}\n"
            f"Fecha de Salida: {self.fecha_salida}\n"
            f"Fecha de Llegada: {self.fecha_llegada}\n"
        )
        return info

    def actualizar_info(self, cliente=None, vuelo=None, fecha_reserva=None, fecha_salida=None, fecha_llegada=None):
        if cliente:
            self.cliente = cliente
        if vuelo:
            self.vuelo = vuelo
        if fecha_reserva:
            self.fecha_reserva = fecha_reserva
        if fecha_salida:
            self.fecha_salida = fecha_salida
        if fecha_llegada:
            self.fecha_llegada = fecha_llegada

    def to_dict(self):
        return {
            "codigo_reserva": self.codigo_reserva,
            "cliente": self.cliente,
            "vuelo": self.vuelo,
            "fecha_reserva": self.fecha_reserva.strftime('%Y-%m-%d') if isinstance(self.fecha_reserva, date) else self.fecha_reserva,
            "fecha_salida": self.fecha_salida.strftime('%Y-%m-%d') if isinstance(self.fecha_salida, date) else self.fecha_salida,
            "fecha_llegada": self.fecha_llegada.strftime('%Y-%m-%d') if isinstance(self.fecha_llegada, date) else self.fecha_llegada,
        }
