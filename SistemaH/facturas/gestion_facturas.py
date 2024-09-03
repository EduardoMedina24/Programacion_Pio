import json
from .factura import Factura

def guardar_facturas(facturas, archivo):
    """
    Guarda una lista de facturas en un archivo JSON.

    Args:
        facturas (list of Factura): Lista de facturas a guardar.
        archivo (str): Ruta del archivo donde se guardarán las facturas.
    """
    with open(archivo, 'w') as f:
        json.dump([factura.__dict__ for factura in facturas], f, indent=4)

def cargar_facturas(archivo):
    """
    Carga una lista de facturas desde un archivo JSON.

    Args:
        archivo (str): Ruta del archivo desde donde se cargarán las facturas.

    Returns:
        list of Factura: Lista de facturas cargadas.
    """
    try:
        with open(archivo, 'r') as f:
            facturas_data = json.load(f)
            return [Factura(**data) for data in facturas_data]
    except FileNotFoundError:
        return []

def buscar_factura(facturas, numero_factura):
    """
    Busca una factura por su número.

    Args:
        facturas (list of Factura): Lista de facturas.
        numero_factura (str): Número de la factura a buscar.

    Returns:
        Factura or None: La factura encontrada o None si no se encuentra.
    """
    for factura in facturas:
        if factura.numero_factura == numero_factura:
            return factura
    return None

def eliminar_factura(facturas, numero_factura):
    """
    Elimina una factura por su número.

    Args:
        facturas (list of Factura): Lista de facturas.
        numero_factura (str): Número de la factura a eliminar.

    Returns:
        bool: True si la factura fue eliminada, False si no se encontró.
    """
    factura = buscar_factura(facturas, numero_factura)
    if factura:
        facturas.remove(factura)
        return True
    return False
