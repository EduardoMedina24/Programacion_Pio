import json
from hoteles.reserva_hotel import ReservaHotel

def guardar_reservas(reservas, archivo):
    """
    Guarda una lista de reservas en un archivo JSON.
    
    :param reservas: Lista de objetos ReservaHotel a guardar.
    :param archivo: Ruta del archivo donde se guardarán las reservas.
    """
    with open(archivo, 'w') as f:
        json.dump([reserva.__dict__ for reserva in reservas], f, indent=4)

def cargar_reservas(archivo):
    """
    Carga reservas desde un archivo JSON.
    
    :param archivo: Ruta del archivo desde donde se cargan las reservas.
    :return: Lista de objetos ReservaHotel cargados. Retorna una lista vacía si el archivo no se encuentra.
    """
    try:
        with open(archivo, 'r') as f:
            reservas_data = json.load(f)
            return [ReservaHotel(**data) for data in reservas_data]
    except FileNotFoundError:
        return []

def buscar_reserva(reservas, codigo_reserva):
    """
    Busca una reserva por código.
    
    :param reservas: Lista de reservas en las que buscar.
    :param codigo_reserva: Código de la reserva a buscar.
    :return: ReservaHotel si se encuentra, o None si no se encuentra.
    """
    for reserva in reservas:
        if reserva.codigo_reserva == codigo_reserva:
            return reserva
    return None

def eliminar_reserva(reservas, codigo_reserva):
    """
    Elimina una reserva por código.
    
    :param reservas: Lista de reservas.
    :param codigo_reserva: Código de la reserva a eliminar.
    :return: True si la reserva se eliminó con éxito, False en caso contrario.
    """
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        reservas.remove(reserva)
        return True
    return False
