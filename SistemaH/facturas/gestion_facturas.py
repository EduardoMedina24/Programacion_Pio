import json
from .factura import Factura


def guardar_facturas(facturas, archivo):
    with open(archivo, 'w') as f:
        json.dump([factura.__dict__ for factura in facturas], f, indent=4)

def cargar_facturas(archivo):
    try:
        with open(archivo, 'r') as f:
            facturas_data = json.load(f)
            return [Factura(**data) for data in facturas_data]
    except FileNotFoundError:
        return []

def buscar_factura(facturas, numero_factura):
    for factura in facturas:
        if factura.numero_factura == numero_factura:
            return factura
    return None

def eliminar_factura(facturas, numero_factura):
    factura = buscar_factura(facturas, numero_factura)
    if factura:
        facturas.remove(factura)
        return True
    return False
