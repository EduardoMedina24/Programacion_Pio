import json
from hoteles.reserva_hotel import ReservaHotel


def guardar_reservas(reservas, archivo):
    with open(archivo, 'w') as f:
        json.dump([reserva.__dict__ for reserva in reservas], f, indent=4)

def cargar_reservas(archivo):
    try:
        with open(archivo, 'r') as f:
            reservas_data = json.load(f)
            return [ReservaHotel(**data) for data in reservas_data]
    except FileNotFoundError:
        return []

def buscar_reserva(reservas, codigo_reserva):
    for reserva in reservas:
        if reserva.codigo_reserva == codigo_reserva:
            return reserva
    return None

def eliminar_reserva(reservas, codigo_reserva):
    reserva = buscar_reserva(reservas, codigo_reserva)
    if reserva:
        reservas.remove(reserva)
        return True
    return False
