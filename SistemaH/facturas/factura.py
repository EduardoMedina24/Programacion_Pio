class Factura:
    def __init__(self, numero_factura, cliente, descripcion, monto_total, fecha_emision):
        self.numero_factura = numero_factura
        self.cliente = cliente
        self.descripcion = descripcion
        self.monto_total = monto_total
        self.fecha_emision = fecha_emision

    def mostrar_info(self):
        return (f"Número de Factura: {self.numero_factura}\n"
                f"Cliente: {self.cliente}\n"
                f"Descripción: {self.descripcion}\n"
                f"Monto Total: {self.monto_total}\n"
                f"Fecha de Emisión: {self.fecha_emision}")

    def actualizar_info(self, cliente=None, descripcion=None, monto_total=None, fecha_emision=None):
        if cliente:
            self.cliente = cliente
        if descripcion:
            self.descripcion = descripcion
        if monto_total:
            self.monto_total = monto_total
        if fecha_emision:
            self.fecha_emision = fecha_emision
