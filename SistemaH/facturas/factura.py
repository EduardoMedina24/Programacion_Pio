class Factura:
    """
    Clase que representa una factura.

    Atributos:
        numero_factura (str): Número de la factura.
        cliente (str): Nombre del cliente.
        descripcion (str): Descripción de la factura.
        monto_total (float): Monto total de la factura.
        fecha_emision (date): Fecha de emisión de la factura.

    Métodos:
        mostrar_info(): Devuelve una cadena con la información de la factura.
        actualizar_info(cliente=None, descripcion=None, monto_total=None, fecha_emision=None): 
            Actualiza los atributos de la factura.
    """
    def __init__(self, numero_factura, cliente, descripcion, monto_total, fecha_emision):
        self.numero_factura = numero_factura
        self.cliente = cliente
        self.descripcion = descripcion
        self.monto_total = monto_total
        self.fecha_emision = fecha_emision

    def mostrar_info(self):
        """
        Devuelve una cadena con la información de la factura.
        """
        return (f"Número de Factura: {self.numero_factura}\n"
                f"Cliente: {self.cliente}\n"
                f"Descripción: {self.descripcion}\n"
                f"Monto Total: {self.monto_total}\n"
                f"Fecha de Emisión: {self.fecha_emision}")

    def actualizar_info(self, cliente=None, descripcion=None, monto_total=None, fecha_emision=None):
        """
        Actualiza los atributos de la factura.

        Args:
            cliente (str, optional): Nuevo nombre del cliente.
            descripcion (str, optional): Nueva descripción de la factura.
            monto_total (float, optional): Nuevo monto total.
            fecha_emision (date, optional): Nueva fecha de emisión.
        """
        if cliente:
            self.cliente = cliente
        if descripcion:
            self.descripcion = descripcion
        if monto_total:
            self.monto_total = monto_total
        if fecha_emision:
            self.fecha_emision = fecha_emision
