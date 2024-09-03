class ReservaHotel:
    def __init__(self, codigo_reserva, cliente, hotel, fecha_reserva, fecha_checkin, fecha_checkout):
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.hotel = hotel
        self.fecha_reserva = fecha_reserva
        self.fecha_checkin = fecha_checkin
        self.fecha_checkout = fecha_checkout

    def mostrar_info(self):
        return (f"Código de Reserva: {self.codigo_reserva}\n"
                f"Cliente: {self.cliente}\n"
                f"Hotel: {self.hotel}\n"
                f"Fecha de Reserva: {self.fecha_reserva}\n"
                f"Fecha de Check-in: {self.fecha_checkin}\n"
                f"Fecha de Check-out: {self.fecha_checkout}")

    def actualizar_info(self, cliente=None, hotel=None, fecha_reserva=None, fecha_checkin=None, fecha_checkout=None):
        if cliente:
            self.cliente = cliente
        if hotel:
            self.hotel = hotel
        if fecha_reserva:
            self.fecha_reserva = fecha_reserva
        if fecha_checkin:
            self.fecha_checkin = fecha_checkin
        if fecha_checkout:
            self.fecha_checkout = fecha_checkout
